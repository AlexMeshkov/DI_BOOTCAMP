// src/App.js
import React, { useState } from 'react';
import './App.css';
import Text from './Text';

function App() {
  const [txt, setTxt] = useState('');

  const handleInputChange = (e) => {
    setTxt(e.target.value);
  };

  return (
    <div className="App">
      <h1>App Component</h1>
      <input
        type="text"
        placeholder="Enter text"
        value={txt}
        onChange={handleInputChange}
      />
      <Text txt={txt} />
    </div>
  );
}

export default App;
