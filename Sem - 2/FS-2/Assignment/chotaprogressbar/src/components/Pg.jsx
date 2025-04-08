import { useState } from "react";
import './pg.css'

function Pg() {
    const [count, setCount] = useState(0)

    function increment(){
        setCount(count+10)
    }

    function decrement(){
        setCount(count-10)
    }

    return (
        <>

            <div id="pg" style={{width:`${count}%`}}></div>
            <p>{count}</p>

            <button onClick={increment}>Add</button>
            <button onClick={decrement}>dec</button>
        </>
    );
}


export default Pg;