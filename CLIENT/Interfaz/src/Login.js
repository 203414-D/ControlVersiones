import {useEffect, useState} from "react";
import axios from 'axios';
import { Link } from "react-router-dom";


const Login = (props) => {

    const [username, setUsername] = useState();
    const [password, setpassword] = useState();

    const post = (url)=>{

        axios.post(url, {'username':username,'password':password},{
            headers:{'Content-Type' : 'application/json',
            'Accept' : 'application/json',}
        })
        .then(response=>{
            console.log(response.data)
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('user_id', response.data.user_id);
            localStorage.setItem('first_name', response.data.first_name);
            localStorage.setItem('last_name', response.data.last_name);
            localStorage.setItem('email', response.data.email);
            localStorage.setItem('username', username)
            var clave = localStorage.getItem('token')
            console.log(localStorage)
            alert("inicio de sesion exitoso")
            window.location="/profile/"+localStorage.getItem('userid')
        })
        .catch((error) => {
            console.log(error)
            alert("error al iniciar sesion, intentelo de nuevo")
        })
    }
    return(
        <div className="login">
            <h2>Logearse</h2>
            <div className="controls">
            <label>username: 
            <input type="text" name="username" onChange={e=>setUsername(e.target.value)}/></label>
            </div>
            <div className="controls">
            <label>Password: 
            <input type="password"name="contraseña" onChange={e=>setpassword(e.target.value)}/>
            </label>
            </div>
            <div className="butons">
            <button onClick={()=>{
                console.log('funcionando')
                post('http://localhost:8000/api/v1/login/')
            }}>Iniciar Sesion</button>
            </div>
            <Link id="Link-Style" to="/register">Registrarse</Link>
        </div>
    )

}
export default Login


