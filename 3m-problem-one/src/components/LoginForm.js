import { useState } from 'react';
import jwt from 'jwt-decode' // import dependency

const LoginForm = function(props) {
  const {setLogged, setToken} = props

  // States for login
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');

  // States for checking the errors
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(false);

  // Handling the name change
  const handleName = (e) => {
    setName(e.target.value);
    setSubmitted(false);
  };

  // Handling the password change
  const handlePassword = (e) => {
    setPassword(e.target.value);
    setSubmitted(false);
  };

  // Handling the form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    let opts = {
      'username': name,
      'password': password,
    }

    fetch('/api/auth/login', {
        method: 'post',
        body: JSON.stringify(opts)
    }).then(r => r.json())
    .then(resp => {
        if (resp.error) {
            alert(resp.error)
            return
        }
        else {
          setToken(resp.access_token)
          setLogged(true)
          // login(resp.access_token)
          //loginTokenAuth(token)
          // open table view
          setSubmitted(true);
        }
    })
  };

  // Showing success message
  const successMessage = () => {
    return (
      <div
        className="success"
        style={{
          display: submitted ? '' : 'none',
        }}>
        <h1>User {name} successfully logged in!!</h1>
      </div>
    );
  };

  return (
    <div className="form">
      <div>
        <h1>User Login</h1>
      </div>

      {/* Calling to the methods */}
      <div className="messages">
        {successMessage()}
      </div>

      <form>
        {/* Labels and inputs for form data */}
        <label className="label">Name</label>
        <input onChange={handleName} className="input"
          value={name} type="text" />

        <label className="label">Password</label>
        <input onChange={handlePassword} className="input"
          value={password} type="password" />

        <button onClick={handleSubmit} className="btn" type="submit">
          Submit
        </button>
      </form>
    </div>
  );
}

export default LoginForm