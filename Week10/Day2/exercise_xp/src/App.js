
import './App.css';
import UserFavoriteAnimals from './components/UserFavoriteAnimals';
import Exercise from './components/Exercise3';

function App() {
  const myel = <h1>I Love JSX</h1>
  const myelement = <h1>"React is {5+5} times better with JSX"!</h1>
  const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};
  return (
    <div className="App">
      <header>
    
        <p>Hello World!</p>
        {myel}
        {myelement}
        <h3>{user.firstName}</h3>
        <h3>{user.lastName}</h3>

        <UserFavoriteAnimals animals={user.favAnimals} />
        <Exercise/>
      </header>
    </div>
  );
}

export default App;
