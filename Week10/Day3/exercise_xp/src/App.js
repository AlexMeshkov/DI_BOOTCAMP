
import Car from './component/Car';
import Events from './component/Events';
import Phone from './component/Phone';
import Color from './component/Color';

const carinfo = { name: "Ford", model: "Mustang" };

function App() {

    return (
      <div className="App">

      <Car MacBook = {carinfo.model}/>
    
      <Events />

      <Phone />

      <Color />
      
    </div>
    );
}

export default App;
