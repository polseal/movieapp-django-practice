import { useState } from "react";

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const submit = async (e: React.FormEvent) => {
        e.preventDefault();
        console.log(username + " " + password);
        try {
            const response = await fetch('http://localhost:8000/authentification/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                password: password,
            }),
            credentials: 'include',
        });
        if (!response.ok) {
            alert(`HTTP error! Status: ${response.status}`);
            return;
        }
        const data = await response.json();
        localStorage.clear();
        localStorage.setItem('access_token', data['access']);
        localStorage.setItem('refresh_token', data['refresh']);
        window.location.href = '/';
        } catch (error) {   
            console.error('Error:', error);
        }
    };
    return (
        <div className="Auth-form-container">
        <form className="Auth-form" onSubmit={submit}>
            <div className="Auth-form-content">
                <h3 className="Auth-form-title">Sign In</h3>
                <div className="form-group mt-3">
                    <label>Username</label>
                    <input
                        className="form-control mt-1"
                        placeholder="Enter Username"
                        name='username'
                        type='text'
                        value={username}
                        required
                        onChange={e => setUsername(e.target.value)}
                    />
                </div>
                <div className="form-group mt-3">
                    <label>Password</label>
                    <input
                        name='password'
                        type="password"
                        className="form-control mt-1"
                        placeholder="Enter password"
                        value={password}
                        required
                        onChange={e => setPassword(e.target.value)}
                    />
                </div>
                <div className="d-grid gap-2 mt-3">
                    <button type="submit" className="btn btn-primary">Submit</button>
                </div>
            </div>
        </form>
    </div>
    );
}
export default Login;