import axios, { Axios } from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Profile(params) {
    const [url, setUrl]= useState();
    var username=localStorage.getItem('username');
    var firstName=localStorage.getItem('first_name');
    var lastName=localStorage.getItem('last_name');
    var Email=localStorage.getItem('email');
    var user_id=localStorage.getItem('user_id');
    useEffect(()=>{
        document.title='Profile'
    });
    let obtenerImagen = (()=>{
        let token = localStorage.getItem('token')
        console.log(token)
        axios.get('http://localhost:8000/api/v2/user/'+localStorage.getItem('user_id'),{
            headers:{
                'Authorization': 'Token '+localStorage.getItem('token'),
            },
        })

        .then((response)=>{
            let urlPro = 'http://localhost:8000'+response.data['url_img']
            setUrl(urlPro)
            console.log(urlPro)
            
        });
    });
    const verificar = (()=>{
        let veri = url
        if (veri !=null) {
            Modificar()
        } else {
            Nueva()
           }
        });
        
        let Nueva = (()=>{
                let datapost = new FormData();
                datapost.append('user_id', localStorage.getItem('user_id'));
                datapost.append('url_img', document.getElementById('img').files[0]);
                axios.post("http://localhost:8000/api/v1/user/", datapost,{
                    headers:{
                        'Content-Type': 'multipart/from-data',
                        'Authorization': 'Token '+localStorage.getItem('token'),
                    }
                })

                .then((response)=>{
                    let urlNew = 'http://localhost:8000'+response.data['url_img']
                    setUrl(urlNew)
                    console.log(urlNew)
                    window.location="/profile/"+localStorage.getItem('user_id')
                })
        });

        let Modificar = (()=>{
                let Putdata = new FormData();
                Putdata.append('user_id', localStorage.getItem('user_id'));
                Putdata.append('url_img', document.getElementById('img').files[0]);
                axios.put("http://localhost:8000/api/v2/user/"+localStorage.getItem('user_id'), Putdata,{
                    headers:{
                        'Content-Type': 'multipart/from-data',
                        'Authorization': 'Token '+localStorage.getItem('token'),
                    }
                })
                .then((response)=>{
                    let urlput = 'http://localhost:8000'+response.data['url_img']
                    setUrl(urlput)
                    console.log(urlput)
                })
                .catch((error)=>{
                    console.log(error)
                    alert("error al ingresar nueva imagem")
                })
        });
    let l=url
    obtenerImagen()
    return(
        <div className="profile">
        <h2>Perfil</h2>
        <div className="image"><img src={l}></img><br></br></div>
        <input accept="image/png,image/jpeg" type="file" id="img"></input>
        <button onClick={()=>{
                console.log('funcionando')
                verificar()
        }}>nueva foto</button>
        <p id="vacio"></p>
        <p><b>id de usuario: </b>{user_id}</p>
        <p><b>username: </b>{username}</p>
        <p><b>first name: </b>{firstName}</p>
        <p><b>last name: </b>{lastName}</p>
        <p><b>email: </b>{Email}</p>
        <Link id="Link-Style" to="/login">volver</Link>
        </div>
        
    );

}
export default Profile