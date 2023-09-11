
import users from "./data.json";
import './App.css';
import {v4 as uuidv4} from "uuid";
import User from './components/Users';
import Button from '@mui/material/Button';

function App() {
  console.log("user=>", users);
  return (
    

    <div className="App">
      <header className="App-header">
        {users.map((item)=>{
          return <User  info={item} key = {uuidv4()}/>;
        })}
 </header>
 </div>
  );
      }


export default App;
