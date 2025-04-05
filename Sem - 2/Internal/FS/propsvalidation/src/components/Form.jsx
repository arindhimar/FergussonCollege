import { useState, useEffect } from "react";

// import './Form.css'

function Form() {
    const [name,setName] = useState("");
    const [email,setEmail]=useState("");
    const [address,setAddress]=useState("");

    function Jadu(e){
        e.preventDefault();

        let ptName = /^[a-zA-Z]{3,}$/;

        if(ptName.test(name.toString())){
            alert("lol")
        }
    }

   return(
    <div>
    <form onSubmit={(e)=>Jadu(e)}>
        <div className="form-field"><label htmlFor="name">Name</label><input type="text" name="name" id="name" value={name} onChange={(e)=>setName(e.target.value)} /></div>
        <div className="form-field"><label htmlFor="email">Email</label><input type="email" name="email" id="email" value={email} onChange={(e)=>setEmail(e.target.value)}/></div>
        <div className="form-field"><label htmlFor="address">Address</label><input type="text" name="address" id="address" value={address} onChange={(e)=>setAddress(e.target.value)}/></div>
        <div className="form-field"><input type="Submit" value="Submit"  /></div>
    </form>

</div>
   );
}

export default Form;