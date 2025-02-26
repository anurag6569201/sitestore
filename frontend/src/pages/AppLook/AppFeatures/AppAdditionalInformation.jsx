import React from "react";
import "./app_styles.css";

const AppAdditionalInformation = () => {
  return (
    <div className="Additional_information mt-4">
      <br />
      <div className="">
        <h5 className="">Additional Information</h5><hr style={{ marginTop: '0', color: 'grey' }} />
        <div className="row">
          <div className="col-md-6">
            <p><strong>Developed by</strong><br /> rocksdanister</p>
            <p><strong>Published by</strong><br /> rocksdanister</p>
            <p><strong>Installation</strong><br /> Get this app while signed in to your Microsoft account and install on up to ten Windows devices.</p>
            <p><strong>Additional terms</strong><br /> <a href="#">Privacy policy</a> | <a href="#">Terms of transaction</a></p>
          </div>
          <div className="col-md-6">
            <p><strong>Approximate size</strong><br /> 941.6 MB</p>
            <p><strong>Category</strong><br /> <a href="#">Personalization</a></p>
            <p><strong>Supported languages</strong><br /> Afrikaans (South Africa), Arabic, Arabic (United Arab Emirates) <a href="#">Read more</a></p>
            <p><strong>Publisher info</strong><br /> <a href="#">Support</a> | <a href="#">Website</a> | <a href="#">Read more</a></p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AppAdditionalInformation;
