import React from 'react';
import Navbar from './Navbar'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

const App = () =>{
  return(
    <Router>
      <Navbar />
    </Router>
  )
}

export default App;