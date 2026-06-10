import express from 'express';
import mongoose, { connect } from 'mongoose';
import Redis from 'ioredis';
import cors from 'cors';
import dotenv from 'dotenv';
dotenv.config();

const app = express();

app.use(express.json());
app.use(cors());


const PORT = process.env.PORT || 3001;
let redisclient = null;
const connectionTomongo = async () => {
    await mongoose.connect(process.env.MONGO_URL ||'mongodb://localhost:27017/mongo_db');
    redisclient = await new Redis(process.env.REDIS_URL || 'redis://localhost:6379');
    console.log('Connected to MongoDB');
}

connectionTomongo().then(() => {
    app.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });
}).catch((err) => {
    console.error('Failed to connect to MongoDB', err);
});

const userSchema = new mongoose.Schema({
    name: String,
    age: Number
});

const User = mongoose.model('User', userSchema);

app.get('/', (req, res) => {
    res.send('contaienr is working fine!');
});


app.post('/api/insert', async (req, res) => {
    const { name, age } = req.body;
    try {
        const user = new User({ name, age });
        await user.save();
        await redisclient.set(name, age, 'EX', 60); // Cache in Redis for 60 seconds
        res.status(201).json({ message: 'User inserted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error inserting user', error });
    }
});

app.get('/api/search', async (req, res) => {
    const { name } = req.query;
    try {
        let age = await redisclient.get(name);
        if (age) {
            return res.json({ name, age, from: 'redis' });
        }
        const user = await User.findOne({ name });
        if (user) {
            await redisclient.set(name, user.age, 'EX', 60); // Cache in Redis for 60 seconds
            return res.json({ name: user.name, age: user.age, from: 'mongodb' });
        }
        res.status(404).json({ message: 'User not found' });
    } catch (error) {
        res.status(500).json({ message: 'Error searching user', error });
    }
});

export default app;