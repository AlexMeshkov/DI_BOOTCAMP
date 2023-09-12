// import React from "react";
// import User from "./components/Users";

// class AppClass extends React.Component{
//     constructor(){
//         super();
//         this.state = {
//             txt: "Hello",
//             users:[]
//         };
//     }
//      const getData = async() => {
//     try{
//       const res = await fetch("https://jsonplaceholder.typicode.com/users");
//       const data = await res.json();
//       console.log(data);
//     }catch (error){
//       console.log("err=>", error);
//     }
    
//   };
//   handleChange = (e)=>{
//     console.log(e.target.value);
//     this.setState({txt: e.target.value});
//   };
//   render(){
//     return (
//         <div>
//             <h1>App class Component</h1>
//             <h2>{this.setState.txt}</h2>
//             <input onChange={this.handleChange}/>
//             <button onClick={this.getData}>Get Users!</button>
//         </div>
//     )
//   }
// }

//       console.log("err=>", error);
    
import React from "react";
import User from "./components/Users";

class AppClass extends React.Component {
  constructor() {
    super();
    this.state = {
      txt: "Hello",
      users: []
    };
  }

  getData = async () => {
    try {
      const res = await fetch("https://jsonplaceholder.typicode.com/users");
      const data = await res.json();
      console.log(data);
    } catch (error) {
      console.log("err=>", error);
    }
  };

  handleChange = (e) => {
    console.log(e.target.value);
    this.setState({ txt: e.target.value });
  };

  render() {
    return (
      <div>
        <h1>App class Component</h1>
        <h2>{this.state.txt}</h2>
        <input onChange={this.handleChange} />
        <button onClick={this.getData}>Get Users!</button>
      </div>
    );
  }
}

export default AppClass;
