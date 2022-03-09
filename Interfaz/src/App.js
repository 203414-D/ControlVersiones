import Login from './Login';
import './estilos.css';
import Register from './Register';
import UserProfile from './UserProfile';
import {BrowserRouter, Switch, Routes,Route} from 'react-router-dom'

function App() {
  return (
    <BrowserRouter>
      <Routes>
            <Route path='' element={<Register></Register>}></Route>
            <Route path='/register' element={<Register></Register>}></Route>
            <Route path='/login' element={<Login></Login>}/>
            <Route path='/profile/:user_id'element={<UserProfile></UserProfile>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
