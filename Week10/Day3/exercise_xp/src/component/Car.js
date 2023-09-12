import  {useState} from "react";
import Garage from "./Garage";

const Car = (props)=>{
const {MacBook} = props
const [color, setcolor]= useState('red');

    

    return (
        <div>
            <h1>This car is {MacBook}, color: {color}</h1>
            <Garage size="small" />
        </div>
    );
}


export default Car;