import React, { useState } from "react";
import User from './components/Users';
import { v4 as uuidv4 } from "uuid";
import Button from '@mui/material/Button';

function App() {
  const [txt, setTxt] = useState(""); // Added state for 'txt'
  const [users, setUsers] = useState([]); // Added state for 'users'

  const getData = async () => {
    try {
      const res = await fetch("https://jsonplaceholder.typicode.com/users");
      const data = await res.json();
      console.log(data);
      setUsers(data);
    } catch (error) {
      console.log("err=>", error);
    }
  };

  const handleChange = (e) => {
    console.log(e.target.value);
    setTxt(e.target.value); // Update 'txt' state when input changes
  };

  return (
    <div>
      <h2>{txt}</h2>
      <input type='text' onChange={(e) => handleChange(e)} />
      <button onClick={getData}>Get Users!</button>

      <div className="App">
        <header className="App-header">
          {users.map((item) => {
            return <User info={item} key={uuidv4()} />;
          })}
        </header>
      </div>
    </div>
  );
}

export default App;

// import users from "./data.json";
// import './App.css';
// import {v4 as uuidv4} from "uuid";
// import User from './components/Users';
// import Button from '@mui/material/Button';

// function App() {

//   const users = []
//   console.log("user=>", users);

//   const getData = async() => {
//     try{
//       const res = await fetch("https://jsonplaceholder.typicode.com/users");
//       const data = await res.json();
//       console.log(data);
//       setUsers(data)
//     }catch (error){
//       console.log("err=>", error);
//     }
    
//   };

//   const handleChange = (e) => {
//     console.log(e.target.value);
//   };
//   return (
// <>
//     <h2>{txt}</h2>
//   <input type='text' onChange = {(e)=>{handleChange(e)}/>
//   <button onClick = {(name)=> getData(e)}> Get Users! </button>
    

//     <div className="App">
//       <header className="App-header">
//         {users.map((item)=>{
//           return <User  info={item} key = {uuidv4()}/>;
//         })}
//  </header>
//  </div>
//   );</>
      


// export default App;
