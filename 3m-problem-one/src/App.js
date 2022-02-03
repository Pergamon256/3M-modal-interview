import './App.css';
import { useState } from 'react';
import RegistrationForm from './components/RegistrationForm'
import LoginForm from './components/LoginForm'
import TableView from './components/TableView';
function App() {
  const [logged, setLogged] = useState(false)
  const [token, setToken] = useState("")

  return (
    <div className="App">
      {logged ?
        <TableView token={token} setLogged={setLogged} />
      :
      <div>
        <RegistrationForm />
        <LoginForm setLogged={setLogged} setToken={setToken}/>
        </div>
      }
    </div>
  );
}

export default App;
