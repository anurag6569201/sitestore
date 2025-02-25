import React from 'react';
import './Rating.css';

export default function Rating() {
  // Default rating data
  const ratingData = {
    average: 4.1,
    totalReviews: 254,
    ratings: [
      { stars: 5, count: 150, width: '60%' },
      { stars: 4, count: 63, width: '30%' },
      { stars: 3, count: 15, width: '10%' },
      { stars: 2, count: 6, width: '4%' },
      { stars: 1, count: 20, width: '15%' },
    ],
  };

  return (
    <div className="rating-container">
      <span className="heading">User Rating</span>
      {[...Array(5)].map((_, i) => (
        <span key={i} className={`fa fa-star ${i < Math.round(ratingData.average) ? 'checked' : ''}`}></span>
      ))}
      <p>{ratingData.average} average based on {ratingData.totalReviews} reviews.</p>
      <hr />

      {ratingData.ratings.map((item) => (
        <div key={item.stars} className="row">
          <div className="side">{item.stars} star</div>
          <div className="middle">
            <div className="bar-container">
              <div className={`bar bar-${item.stars}`} style={{ width: item.width }}></div>
            </div>
          </div>
          <div className="side right">{item.count}</div>
        </div>
      ))}
    </div>
  );
}
