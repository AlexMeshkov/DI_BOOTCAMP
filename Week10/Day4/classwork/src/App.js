import "./App.css";
import Parent from "./components/Parent";
import Child from "./components/Child";

function App(){
  return(
    <>
      <Parent user ="aaa">
      <Child/>
      </Parent>
    </>
  );
}

export default App;