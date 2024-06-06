import { } from 'react';
import { Link } from 'react-router-dom';
import '../css/style.scss';
import Logo from '../assets/logo.png';

function Nav() {
  function navResp() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }
  return (
    <>
      <header>
        <nav className="topnav" id="myTopnav">
          <div className="topnav">
            <a className="navbar-brand disabled" aria-disabled="true">
              <img id='logo' src={Logo} /></a>
            <Link to="/Home" className="tlink">
              Home
            </Link>
            <Link to="/Tracking" className="tlink">
              Tracking
            </Link>
            <Link to="/Info" className="tlink">
              Info
            </Link>
            <a href="javascript:void(0);" className="icon" onClick={navResp}>
              <i className="bi bi-list"></i>
            </a>
          </div>
        </nav>
      </header>
    </>
  );
}
export default Nav;
