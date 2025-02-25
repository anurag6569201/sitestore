import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './navbar.css';
import Logo_img from './images/logo_dark.png';

function Navbar() {
    return (
        <div id="nav-bar">
            <input id="nav-toggle" type="checkbox" />
            <div id="nav-header">
                <Link id="nav-title" to="/"><img src={Logo_img} height='70px' alt="Logo" /></Link>
                <label htmlFor="nav-toggle"><span id="nav-toggle-burger"></span></label>
                <hr />
            </div>
            <div id="nav-content">
                <Link className="nav-button" to="/"><i className="fas fa-palette"></i><span>Discover</span></Link>
                <Link className="nav-button" to="/updates"><i className="fas fa-thumbtack"></i><span>Pinned Items</span></Link>
                <hr />
                <Link className="nav-button" to="/trending"><i className="fas fa-chart-line"></i><span>Trending</span></Link>
                <Link className="nav-button" to="/types"><i className="fas fa-magic"></i><span>Spark</span></Link>
                <Link className="nav-button" to="/look"><i className="fas fa-magic"></i><span>App Look</span></Link>
                <div id="nav-content-highlight"></div>
            </div>
            <input id="nav-footer-toggle" type="checkbox" />
            <div id="nav-footer">
                <div id="nav-footer-heading">
                    <div id="nav-footer-avatar"><img src="https://gravatar.com/avatar/4474ca42d303761c2901fa819c4f2547" alt="Avatar" /></div>
                    <div id="nav-footer-titlebox">
                        <a id="nav-footer-title" href="https://codepen.io/uahnbu/pens/public" target="_blank" rel="noopener noreferrer">uahnbu</a>
                        <span id="nav-footer-subtitle">Admin</span>
                    </div>
                    <label htmlFor="nav-footer-toggle"><i className="fas fa-caret-up"></i></label>
                </div>
                <div id="nav-footer-content">
                    ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </div>
            </div>
        </div>
    );
}

export default Navbar;
