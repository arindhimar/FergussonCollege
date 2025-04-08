import { useState } from 'react'

function Counter() {
    const [count, setCount] = useState(0)
    return (
        <>
        <p>count is {count}</p>
            <button onClick={() => setCount((count) => count + 1)}>
                Add
            </button>
            <button onClick={() => setCount((count) => count - 1)}>
                dec
            </button>
        </>
    );
}

export default Counter;