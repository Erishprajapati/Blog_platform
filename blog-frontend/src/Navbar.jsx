import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary px-3">
      <div className="container-fluid">
        
        <a className="navbar-brand fw-bold" href="#">
         <img src="mindrisers/image/Screenshot 2025-02-13 at 06.37.47.png" alt="logo" height={40} />

        </a>

        {/* Navbar Toggler Button for Mobile */}
        <button 
          className="navbar-toggler" 
          type="button" 
          data-bs-toggle="collapse" 
          data-bs-target="#navbarNav" 
          aria-controls="navbarNav" 
          aria-expanded="false" 
          aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>

    
        <div className="collapse navbar-collapse" id="navbarNav">

          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <a className="nav-link text-white" href="#">Home</a>
            </li>
            <li className="nav-item">
              <a className="nav-link text-white" href="#">Create Post</a>
            </li>
            <li className="nav-item">
              <a className="nav-link text-white" href="#">Saved Posts</a>
            </li>
            <li className="nav-item">
              <button className="btn btn-light ms-3">Account</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
