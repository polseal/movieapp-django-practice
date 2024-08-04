import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { useState, useEffect} from 'react';

export function Navigator() {
    const [isAuth, setIsAuth] = useState(false);

    useEffect(() => {
        if (localStorage.getItem('access_token') !== null) {
            setIsAuth(true); 
          }
    }, [isAuth]);

    return (
        <div>
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="/">Movie Catalog</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto"> 
            {isAuth ? <Nav.Link href="/">Home</Nav.Link> : null}
            </Nav>
            <Nav>
            {isAuth ? <Nav.Link href="/logout">Logout</Nav.Link> :  
                        <Nav.Link href="/login">Login</Nav.Link>}
            </Nav>
            </Navbar.Collapse>
        </Navbar>
        </div>
    );
}

export default Navigator;