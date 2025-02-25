import React from "react";

const AppAdditionalInformation = () => {
  return (
    <div className="container mt-4">
      <div className="card p-4 bg-dark text-white">
        <h5 className="mb-3">Additional Information</h5>
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
        <div className="row mt-3">
          <div className="col-md-6">
            <p><strong>Report this product</strong><br /> <a href="#">Report this product for violating Microsoft Store Policy</a><br /> <a href="#">Report this product for illegal content</a></p>
          </div>
          <div className="col-md-6">
            <p><strong>App badge</strong><br /> <a href="#">Create app badge</a></p>
            <p><strong>Legal Disclaimer</strong><br /> This seller has certified that it will only offer products or services that comply with all applicable laws.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AppAdditionalInformation;
