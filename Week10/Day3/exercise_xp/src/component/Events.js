import {useState} from 'react'


const clickMe = ()=> {
        alert('I was clicked');
    }

const handleKeyDown = (e)=>{
    if (e.key === 'Enter'){
        alert('You pressed Enter with value: '+ e.target.value);
    }
}

const Events = () => {
    const [isToggleOn, setIsToggleOn]= useState("ON");

    const toggleState = ()=>{
        setIsToggleOn(prevState => !prevState);
    }


    return(
        <div>
            <button onClick = {clickMe}>Click me!</button>
            
            <input type="text" onKeyDown={handleKeyDown} placeholder="Type something and press Enter"/>

            <button onClick={toggleState}>
                {isToggleOn ? "ON"  :  "OFF"}
            </button>

        </div>
    );
}
export default Events;