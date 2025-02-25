import * as React from 'react';
import ImageCategory1 from '../../pages/ui/ImageCategory1.jsx';
import Rating from './Rating.jsx';
import Comments from './Comments.jsx';
import './ImgMediaCard.css'; // Import the external CSS file

export default function ImgMediaCard() {
  return (
    <div className="mat">
      {/* Left Section */}
      <div className="left">
        {/* Logo Section */}
        <div className="leftContent">
          <div className="leftText">
            {/* Logo Box */}
            <div className="logoContainer">
              <div className="logoBox">Logo box</div>
            </div>

            {/* Left Section Text */}
            <div>
              <h1>Left Section</h1>
              <p>This is the left side content.</p>
            </div>
          </div>

          {/* Visit Button */}
          <button className="button">Visit</button>
        </div>

        {/* Screenshots Section */}
        <div className="sectionContainer">
          <h1>SCREENSHOTS</h1>
          <ImageCategory1 />
        </div>

        {/* Rating Section */}
        <div className="sectionContainer">
          <Rating />
        </div>

        {/* Comments Section */}
        <div className="sectionContainer">
          <Comments />
        </div>
      </div>

      {/* Right Section */}
      <div className="right">
        <div className="cards">
          <h1>Right Section</h1>
          <p>This is the right side content.</p>
        </div>
        <div className="cards">
          <h2>Additional Card</h2>
          <p>Some additional information.</p>
        </div>
        <div className="cards">
          <h2>Another Card</h2>
          <p>More details here.</p>
        </div>
      </div>
    </div>
  );
}
