import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'

import Navbar from './pages/global/navbar/navbar'
import Discover from './pages/Discover/Discover';
import WebTrending from './pages/WebTrending/WebTrending';
import WebTypes from './pages/WebTypes/WebTypes';
import WebUpdates from './pages/WebUpdates/WebUpdates';

function App() {

  return (
    <>
      <Router>
        <div className="MainSpace">
          <div className="NavbarSpace">
            <Navbar />
          </div>
          <div className="ContentSpace">
            <Routes>
              <Route path="/" element={Discover()} />
              <Route path="/updates" element={WebUpdates()} />
              <Route path="/trending" element={WebTrending()} />
              <Route path="/types" element={WebTypes()} />
            </Routes>
          </div>
        </div>
      </Router>
    </>
  )
}

export default App
