import { useState } from "react";

function Counter(){
    const [count,setCount] = useState(0);

    return(<>
        <div id="pg" style={{width:`${count}%`}}></div>
        <button onClick={()=>setCount(count+10)}>add</button>
        <button  onClick={()=>setCount(count-10)}>min</button>
    </>);
}

export default Counter;