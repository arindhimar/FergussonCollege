import { useState } from "react";

function Counter(){
    const [count,setCount] = useState(0);

    return(<>
        
        <button onClick={()=>setCount(count+1)}>add</button>
        <button  onClick={()=>setCount(count-1)}>min</button>
    </>);
}

export default Counter;