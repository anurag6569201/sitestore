import './app_styles.css'
import './RatingReview.css'

import AllRatingsReviews from './AllRatingsReviews';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

function AppRatings() {
    return (
        <>
            <div className="app_ratings">
                <br />
                <h5>Ratings</h5><hr style={{ marginTop: '0', color: 'grey' }} />
                <div class="container">
                    <div class="row">
                        <div class="col-md-12 course-details-content p-0 m-0">
                            <div class="course-details-card mt--40">
                                <div class="course-content">
                                    <div class="row row--30">
                                        <div class="col-lg-4">
                                            <div class="rating-box">
                                                <div class="rating-number">5.0</div>
                                                <div class="rating"> <i class="fa fa-star" aria-hidden="true"></i> <i class="fa fa-star" aria-hidden="true"></i> <i class="fa fa-star" aria-hidden="true"></i> <i class="fa fa-star" aria-hidden="true"></i> <i class="fa fa-star" aria-hidden="true"></i> </div>
                                                <span>(25 Review)</span> </div>
                                        </div>
                                        <div class="col-lg-8">
                                            <div class="review-wrapper">
                                                <div class="single-progress-bar">
                                                    <div class="rating-text"> 5 <i class="fa fa-star" aria-hidden="true"></i> </div>
                                                    <div class="progress">
                                                        <div class="progress-bar" role="progressbar" style={{width:'100%'}} aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                                    </div>
                                                    <span class="rating-value">23</span> </div>
                                                <div class="single-progress-bar">
                                                    <div class="rating-text"> 4 <i class="fa fa-star" aria-hidden="true"></i> </div>
                                                    <div class="progress">
                                                        <div class="progress-bar" role="progressbar" style={{width:'80%'}} aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                                                    </div>
                                                    <span class="rating-value">3</span> </div>
                                                <div class="single-progress-bar">
                                                    <div class="rating-text"> 3 <i class="fa fa-star" aria-hidden="true"></i> </div>
                                                    <div class="progress">
                                                        <div class="progress-bar" role="progressbar" style={{width:'60%'}} aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                                                    </div>
                                                    <span class="rating-value">2</span> </div>
                                                <div class="single-progress-bar">
                                                    <div class="rating-text"> 2 <i class="fa fa-star" aria-hidden="true"></i> </div>
                                                    <div class="progress">
                                                        <div class="progress-bar" role="progressbar" style={{width:'40%'}} aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                                                    </div>
                                                    <span class="rating-value">3</span> </div>
                                                <div class="single-progress-bar">
                                                    <div class="rating-text"> 1 <i class="fa fa-star" aria-hidden="true"></i> </div>
                                                    <div class="progress">
                                                        <div class="progress-bar" role="progressbar" style={{width:'20%'}} aria-valuenow="0" aria-valuemin="80" aria-valuemax="100"></div>
                                                    </div>
                                                    <span class="rating-value">2</span> </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="comment-wrapper mt-3">
                                        <div class="edu-comment">
                                            <div class="comment-content">
                                            {/* <div class="thumbnail"> <img src="/vite.svg" alt="Comment Images" /> </div> */}
                                                <div class="comment-top">
                                                    <h6 class="title">CSS Tutorials</h6>
                                                    <div class="rating"> <i class="fa fa-star" aria-hidden="true"></i> <i class="fa fa-star" aria-hidden="true"></i><i class="fa fa-star" aria-hidden="true"></i><i class="fa fa-star" aria-hidden="true"></i><i class="fa fa-star" aria-hidden="true"></i> </div>
                                                </div>
                                                <span class="subtitle">“ Outstanding Review Design ”</span>
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                            </div>
                                        </div>
                                        <button type="button" class="review_rating_model_btn btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                                            Read More ...
                                        </button>
                                        <AllRatingsReviews/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default AppRatings;