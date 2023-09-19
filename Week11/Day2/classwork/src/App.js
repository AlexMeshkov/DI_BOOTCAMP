import Shop from './components/Shop';
import './App.css';

function App() {
  return (
    <div className="App">
     <nav>
      <Link to="/">Home</Link><Link to="about">About</Link>{" "}
      <Link to="shop">Shop</Link>
     </nav>
     
    </div>
  );
}

export default App;
