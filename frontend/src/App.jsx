import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

import './App.css'

import Navbar from './pages/global/navbar/navbar'
import HomeSlider from './pages/global/slider/HomeSlider'

function App() {

  return (
    <>
      <Navbar/>
      <HomeSlider/>
    </>
  )
}

export default App
