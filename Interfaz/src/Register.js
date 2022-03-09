import {useEffect, useState} from "react";
import axios from 'axios';
import { Link } from "react-router-dom";


const url_register= 'http://localhost:8000/api/v2/register/'


const Register = (props) => {

    const [username, setUsername] = useState();
    const [email, setEmail]= useState();
    const [password, setpassword] = useState();
    const [password2, setpassword2]= useState();
    const [first_name, setFirstName]= useState();
    const [last_name, setLastName]= useState();

    const post = (url)=>{

        axios.post(url, {'username':username,'password':password,'password2':password2,'email':email,'first_name':first_name,'last_name':last_name}).then(response=>{
             console.log(response.data)
        },{
            headers:{
                'Content-Type' : 'application/json',
                'Accept' : 'application/json',}
        })
        .then((response)=>{
            console.log(response.data.token)
            alert("usuario registrado correctamente")
        })
        .catch((error)=>{
            console.log(error.response.data.password[0]);
            console.log(error.response.data.username[0]);
            alert("Error al registrarse, intentelo de nuevo")
        })
        
    }
    return(
        <div className="register">
            <h2>Registrarse</h2>
            <label>username: 
            <input type="text" name="username" onChange={e=>setUsername(e.target.value)}/>
            </label>
            <label>password:
            <input type="password"name="password" onChange={e=>setpassword(e.target.value)}/>
            </label>
            <label>password2:
            <input type="password"name="password2" onChange={e=>setpassword2(e.target.value)}/>
            </label>
            <label>email:
            <input type="email"name="correo" onChange={e=>setEmail(e.target.value)}/>
            </label>
            <label>first name:
            <input type="text" name="first_name" onChange={e=>setFirstName(e.target.value)}/>
            </label>
            <label>last name:
            <input type="text" name="last_name" onChange={e=>setLastName(e.target.value)}/>
            </label>
            <button onClick={()=>{
                console.log('funcionando')
                post(url_register)
            }}>Registrarse</button>
            <Link id="Link-Style"to="/login">logearse</Link>
        </div>
        
    )

}
export default Register