import React from 'react';

class Counter extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            count : Number(this.props.count)
        }
    }

    increment = ()=>{
        this.setState({ count: this.state.count + 1 });
    }
    decrement = ()=>{
        this.setState({ count: this.state.count - 1 });
    }

    render(){
        return(<>
            <p>{this.state.count}</p>
            <button onClick={this.increment}>Add</button>
            <button onClick={this.decrement}>Dec</button>
            </>
        );
    }


}

export default Counter;