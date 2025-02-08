import React, { useState,useEffect } from 'react';

export default function First() {
    const [count,setCount] = useState(0);   
    
    useEffect(()=>{
        alert("Component is mounted!!!");
    },[count]);

    // useEffect(function(){
    //     alert("Component is mounted!!!");
    // },[count]);

    return(
        <>
            <h1>Counter</h1>
            <p>{count}</p>
            <button onClick={()=>setCount(count+1)}>Increment</button>
            <button onClick={()=>setCount(count-1)}>Decrement</button>
        </>
    );

}
