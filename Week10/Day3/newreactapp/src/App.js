import React, { useState } from 'react';
import './App.css';
import Text from './Component/Text';

function App() {
  const [txt, setTxt] = useState(""); // Initialize txt state

  const handleChange = (e) => {
    setTxt(e.target.value); // Update txt state when input changes
  };

  return (
    <div className="App">
      <h1>App Component</h1>
      <input
        type='text'
        value={txt}
        onChange={handleChange}
      />
      <Text txt={txt} /> {/* Pass txt state as a prop to Text component */}
    </div>
  );
}

export default App;






// import React, { useState } from 'react';
// import './App.css';
// import Text from './Component/Text';

// function App() {
//   const [txt, setTxt] = useState(""); // Initialize txt state

//   const handleChange = (e) => {
//     setTxt(e.target.value); // Update txt state when input changes
//   };
//   // useEffect(()=>{
//   //   console.log("HI");
//   // })
//   return (
//     <div className="App">
//       <h1>App Component</h1>
//       <input
//         type='text'
//         value={txt}
//         onChange={handleChange}
//       />
//       <Text txt={txt} /> {/* Pass txt state as a prop to Text component */}
//     </div>
//   );
// }

// export default App;




// // import logo from './logo.svg';
// // import './App.css';

// // function App() {
// //   return (
// //     <div className="App">
// //       <header className="App-header">
// //         <img src={logo} className="App-logo" alt="logo" />
// //         <p>
// //           Edit <code>src/App.js</code> and save to reload.
// //         </p>
// //         <a
// //           className="App-link"
// //           href="https://reactjs.org"
// //           target="_blank"
// //           rel="noopener noreferrer"
// //         >
// //           Learn React
// //         </a>
// //       </header>
// //     </div>
// //   );
// // }

// // export default App;
