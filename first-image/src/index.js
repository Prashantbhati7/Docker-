import express from 'express';

const app = express();

app.get('/', (req, res) => {
  res.send('Hello World! This is the first image! ');
});

app.get('/test', (req, res) => {
  res.send('Docker is working! This is the first image! ');
});


app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
