import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

import './App.css'

import Navbar from './pages/global/navbar/navbar'
import HomeSlider from './pages/global/slider/HomeSlider'
import Category from './pages/category/Category';
import TopSearch from './pages/global/TopSearch/TopSearch';

function App() {

  return (
    <>
    <div className="MainSpace">
      <div className="NavbarSpace">
        <Navbar/>
      </div>
      <div className="ContentSpace">
        <TopSearch/>
        <br />
        <HomeSlider/>
        <Category/>
      </div>
    </div>
    </>
  )
}

export default App
