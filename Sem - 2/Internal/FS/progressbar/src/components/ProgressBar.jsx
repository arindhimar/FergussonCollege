import './ProgressBar.css';

import { useState } from 'react';

function ProgressBar() {

    const [tempwidth, setTempWidth] = useState(0);

    function lolIncrease() {
        if (tempwidth < 100) {
            setTempWidth(tempwidth + 10);
        }

        // document.getElementsByClassName("progress-bar").style.width = tempwidth;
    }

    function lolDecrease() {
        if (tempwidth > 0) {
            setTempWidth(tempwidth - 10);
        }

        // document.getElementsByClassName("progress-bar").style.width = tempwidth;

    }

    return (
        <div className="progress-bar-container">
            <div className="progress-bar" style={{ width: `${tempwidth}%` }}>

            </div>

            <button onClick={lolIncrease}>Increment</button>
            <button onClick={lolDecrease}>Decrement</button>

        </div>
    )
}


export default ProgressBar;
