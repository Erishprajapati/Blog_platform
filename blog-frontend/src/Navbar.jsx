import React from 'react';
import './index.css'; // Import the custom CSS file

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        {/* Left-aligned logo */}
        <a className="navbar-brand" href="#">Blog Platform</a>

        {/* Right-aligned links */}
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav ms-auto"> {/* ms-auto is used to push items to the right */}
            <a className="nav-link active" aria-current="page" href="#">Home</a>
            <a className="nav-link" href="#">Create Post</a>
            <a className="nav-link" href="#">Saved Posts</a>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
