import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Navigator.css';

export function Navigator() {
    const [isAuth, setIsAuth] = useState(false);

    useEffect(() => {
        if (localStorage.getItem('access_token') !== null) {
            setIsAuth(true); 
          }
          console.log('isUTH ' + isAuth);
    }, [isAuth]);

    return (
        <Navbar bg="dark" variant="dark" expand="lg">
        
        <Navbar.Brand as={Link} to="/" className="navbar-header">
        My MovieApp
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ml-auto">
          <Nav.Link as={Link} to="/">Home</Nav.Link>
          {isAuth ? <Nav.Link as={Link} to="/logout">Logout</Nav.Link> :
          <Nav.Link as={Link} to="/login">Login</Nav.Link>}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
    );
}

export default Navigator;