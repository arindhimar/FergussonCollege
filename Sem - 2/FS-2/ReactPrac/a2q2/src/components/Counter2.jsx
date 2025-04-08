import React from "react";
import './fun.css'

class Counter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0,
        }
    }

    increment = () => { this.setState({ count: this.state.count + 1 }) }
    decrement = () => { this.setState({ count: this.state.count - 1 }) }



    render() {
        return (
            <>
                <div id="pg" style={{ width: `${this.state.count}%` }}></div>
                <p>{this.state.count}</p>
                <button onClick={this.increment}>Add</button>
                <button onClick={this.decrement}>dec</button>
            </>
        );
    }
}

export default Counter;