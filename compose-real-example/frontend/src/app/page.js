
'use client'

import { useState } from 'react';

export default function Home() {
  const [name,setName] = useState('');
  const [age,setAge] = useState('');
  const [to_search,setToSearch] = useState('');
  const [search_result,setSearchResult] = useState(null);
  const insert_into_redis_and_db = async (name,age) => {
    const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/insert`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, age }),
    });
    const data = await response.json();
    
  };
  const search = async (name) => {
    const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/search?name=${name}`);
    const data = await response.json();
    setSearchResult(data);
  };
  return (
    search_result ? <div className="container flex flex-col items-center justify-center min-h-screen w-full gap-4 mx-auto p-4">
      <h1>Search Result</h1>
      {search_result.message ? <><p>{search_result.message}</p> <button onClick={() => setSearchResult(null)}>Back</button>  </> : 
      <>
      <p>Name: {search_result.name}</p>
      <p>Age: {search_result.age}</p>
      <p> Got From : {search_result.from} </p>
      <button onClick={() => setSearchResult(null)}>Back</button>
      </>
       }
      </div> : <div className="container flex flex-col items-center justify-center min-h-screen w-full gap-4 mx-auto p-4">

      <h1>This one is to test if the frontend container is able to communicate with the backend container and backend with db containers </h1>
      <p>Testing paragraph to check the layout.</p>
      <input type="text" placeholder="enter your name " value={name} onChange={(e) => setName(e.target.value)} />
      <input type="text" placeholder="enter your age " value={age} onChange={(e) => setAge(e.target.value)} />
      <button onClick={() => insert_into_redis_and_db(name, age)}>Submit</button>
      <h2> search Your data Here ..... </h2>
      <input type="text" placeholder="enter your name to search " value={to_search} onChange={(e) => setToSearch(e.target.value)} />
      <button onClick={() => search(to_search)}>Search</button>
    </div>
  );
}
