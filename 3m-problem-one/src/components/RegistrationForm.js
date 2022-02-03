import { useState } from 'react';

export default function RegistrationForm() {

  // States for registration
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [password, setPassword] = useState('');

  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(false);

  const handleName = (e) => {
    setName(e.target.value);
    setSubmitted(false);
  };

  const handleAge = (e) => {
    setAge(e.target.value);
    setSubmitted(false);
  };

  const handlePassword = (e) => {
    setPassword(e.target.value);
    setSubmitted(false);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    let opts = {
      'username': name,
      'password': password,
      'age': age
    }

    fetch('/api/auth/register', {
        method: 'post',
        body: JSON.stringify(opts)
    }).then(r => r.json())
    .then(resp => {
        if (resp.error) {
            alert(resp.error)
            setError(true)
            return
        }
        else {
            setSubmitted(true);
            setError(false)
        }
    })
  };

  const successMessage = () => {
    return (
      <div
        className="success"
        style={{
          display: submitted ? '' : 'none',
        }}>
        <h1>User {name} successfully registered!!</h1>
      </div>
    );
  };

  const errorMessage = () => {
    return (
      <div
        className="error"
        style={{
          display: error ? '' : 'none',
        }}>
        <h1>Please enter all the fields</h1>
      </div>
    );
  };

  return (
    <div className="form">
      <div>
        <h1>User Registration</h1>
      </div>

      <div className="messages">
        {errorMessage()}
        {successMessage()}
      </div>

      <form>
        <label className="label">Name</label>
        <input onChange={handleName} className="input"
          value={name} type="text" />

        <label className="label">Age</label>
        <input onChange={handleAge} className="input"
          value={age} type="text" />

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