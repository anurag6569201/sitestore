import * as React from 'react';
import './ImgMediaCard.css';

import AppScreenshot from './AppFeatures/AppScreenshot';
import AppDescription from './AppFeatures/AppDescription';
import AppRatings from './AppFeatures/AppRatings';
import AppFeatures from './AppFeatures/AppFeatures';
import AppAdditionalInformation from './AppFeatures/AppAdditionalInformation';

import CategoryFooter from '../category/CategoryFooter';
import AppSidebarSuggestion from './AppFeatures/AppSiderbarSuggestion';

export default function ImgMediaCard() {
  return (
    <>
      <div className="app_overview_space">
        <div className="app_overview" style={{ marginTop: '20px' }}>
          <div className="app_overview_overlay app_overview_overlay_left"></div>
          <div className="app_overview_overlay app_overview_overlay_right"></div>
          <div className="app_overview_overlay app_overview_overlay_down"></div>
        </div>
        <div className="card app_overview_intro">
          <div className="d-flex align-items-center">
            <img
              src="https://avatars.githubusercontent.com/u/29775807?s=200&v=4"
              className="me-3"
              alt="Lively Wallpaper"
              width="50"
              height="50"
              style={{ borderRadius: '10px' }}
            />
            <h2 className="mb-0">Lively Wallpaper</h2>
          </div><br />
          <p className="text-primary mt-2 p-0 m-0">rocksdanister</p>
          <div className="d-flex align-items-center mb-2">
            <span className="me-1">⭐ 4.1</span>
            <span className="text">| 7.11K ratings |</span>
            <a href="#" className="ms-2 text-primary">
              Personalization
            </a>
          </div>
          <div className="d-flex align-items-center">
            <div
              className="border px-2 py-1 text-white"
              style={{ borderRadius: "5px", backgroundColor: "rgba(255, 255, 255, 0.1)" }}
            >
              <strong>ARC 3+</strong>
            </div>
            <span className="ms-2">3+</span>
          </div>
          <p className="mt-3">
            Free and open-source software that allows users to set animated and interactive desktop wallpapers.
          </p>
          <button className="btn app_overview_intro_btn">Share</button>
        </div>
      </div>
      <div className="row" style={{ zIndex: '100' }}>
        {/* <div className="col-md-9" style={{ zIndex: '1000',position:'sticky',top:'20px' }}>
          <div class="app-card mb-3">
            <div class="app-icon">VK</div>
            <div class="app-info">
              <div class="app-title">Photo Map for Vk</div>
              <div class="app-category">0.0 ★ Social</div>
            </div>
            <div class="free-badge">Share</div>
          </div>
        </div> */}
        <div className="col-md-9" style={{ zIndex: '100' }}>
          <AppScreenshot />
          <AppDescription />
          <AppRatings />
          <AppFeatures />
          <AppAdditionalInformation />
        </div>
        <div className="col-md-3" style={{ zIndex: '100' }}>
          <AppSidebarSuggestion />
        </div>
      </div>
      <CategoryFooter />
    </>
  );
}
