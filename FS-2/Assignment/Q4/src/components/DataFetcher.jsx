import React from 'react';



class DataFetcher extends React.Component {
  state = {
    data: null
  };

  componentDidMount() {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(response => response.json())
      .then(data => this.setState({ data }));
  }

  render() {
    return (
      <div>
        <h1>Todo List</h1>
        <ul>
            {this.state.data &&
                this.state.data.map(todo => (
                <li key={todo.id}>{todo.title}</li>
                ))}
        </ul>
        </div>
    );
  }
}


export default DataFetcher;