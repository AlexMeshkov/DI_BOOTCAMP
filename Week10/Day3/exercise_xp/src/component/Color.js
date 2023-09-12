import {useState, useEffect} from 'react';

const Color = () => {
    const [favoriteColor, setFavoriteColor] = useState('red');

const changeColor = ()=>{
    setFavoriteColor("Blue")
}

useEffect(() => {
    alert("useEffect reached");
    setFavoriteColor("Yellow")
}, []);

return (
    <div>
        <h1>My favorite color is {favoriteColor}</h1>
        <button onClick={changeColor}>Change color</button>
    </div>
);
}

export default Color;