import React from 'react'

class Form extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            name: "",
            email: "",
            phone: ""
        }
    }

    test = function (e) {
        e.preventDefault()
        console.log(this.state.name)
        console.log(this.state.email)
        sole.log(this.state.phone)
    }

    nameValidation = (e) => {

        let name = e.target.value
        this.setState({ name: e.target.value })
        let ptname = /^[a-zA-Z]{2,}$/;
        console.log(ptname.test(name))
    }

    emailChange = (e) => {
        this.setState({
            email: e.target.value
        })

        console.log(this.state.email)
        // console.log(e.target.value)
        // console.log("Lol this workls")
    }

    render() {
        return (
            <>
                <form>
                    <input type="text" onChange={(e) => this.nameValidation(e)} id='name' />
                    <br />
                    <input type="text" onChange={(e) => this.emailChange(e)} id='email' />
                    <br />
                    <input type="text" onChange={(e) => this.setState({ phone: e.target.value })} value={this.state.phone} id='phone' />
                    <br />
                    <button onClick={(e) => { this.test(e) }}>Submit</button>
                </form>
            </>
        );
    }

}


export default Form;