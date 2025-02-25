import React from 'react';
import './Comments.css';

export default function Comments() {
  // Default comments data
  const commentsData = [
    {
      id: 1,
      name: 'John Doe',
      comment: 'This is an amazing product! Highly recommend it.',
      likes: 12,
      dislikes: 2,
      profilePic: 'https://i.pravatar.cc/50?img=1',
      time: '2 hours ago',
    },
    {
      id: 2,
      name: 'Jane Smith',
      comment: 'It works well, but I wish it had more features.',
      likes: 8,
      dislikes: 1,
      profilePic: 'https://i.pravatar.cc/50?img=2',
      time: '4 hours ago',
    },
    {
      id: 3,
      name: 'Mike Johnson',
      comment: 'Not satisfied with the experience. Needs improvement!',
      likes: 3,
      dislikes: 7,
      profilePic: 'https://i.pravatar.cc/50?img=3',
      time: '1 day ago',
    },
  ];

  return (
    <div className="comments-section">
      <h2>Comments</h2>
      {commentsData.map((comment) => (
        <div key={comment.id} className="comment">
          <img src={comment.profilePic} alt={comment.name} className="profile-pic" />
          <div className="comment-content">
            <h4>{comment.name} <span className="comment-time">{comment.time}</span></h4>
            <p>{comment.comment}</p>
            <div className="comment-actions">
              <button className="like-btn">👍 {comment.likes}</button>
              <button className="dislike-btn">👎 {comment.dislikes}</button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
