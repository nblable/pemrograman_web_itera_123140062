import React from 'react';
import { Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="container nav-container">
        <div className="logo">
          <Link to="/">Manajemen Buku</Link>
        </div>
        <ul className="nav-links">
          <li><Link to="/">Beranda</Link></li>
          <li><Link to="/stats">Statistik</Link></li>
        </ul>
      </div>
    </nav>
  );
}

Navbar.propTypes = {};

export default Navbar;