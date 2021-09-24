import {Navbar, Nav} from "react-bootstrap";

function TopBar() {
    return (
        <Navbar bg="dark" variant="dark" expand="lg" style={{fontSize:"120%"}}>
            <Navbar.Brand href="/">Alexandry Library</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
                {/* <Nav activeKey={window.location.pathname} className="mr-auto">
                    <Nav.Link href="/">Home</Nav.Link>
                    <Nav.Link href="/ajout">Ajout</Nav.Link>
                    <Nav.Link href="/plats">Plats</Nav.Link>
                    <Nav.Link href="/desserts">Dessert</Nav.Link>
                </Nav> */}
            </Navbar.Collapse>
        </Navbar>
    );
}

export default TopBar;
