function CreateListing() {
    return (
      <div id="new-listing">
          <h1>New Listing</h1>
          <form action="/create_listing" method="POST" encType="multipart/form-data" id="listing-form">
              <h3>Item Info</h3>
              <p>Photos: 
                  <input type="file" name="listing-image" accept="image/*" required/>
                </p>
              <p>Title <input type="text" name="item_name"/></p>
              <p>Description <textarea name="description" id="listing-form"/></p>
              <div className="price">Price: <input type="text" name="price"/></div>
              <div className ="address">
                  <h4>Address</h4>
                  <p>Street address (include unit #): <input type="text" name="street_address"/> </p>
                  <p>City: <input type="text" name="city"/> State: <input type="text" name="state"/> Zipcode: <input type="text" name="zipcode"/> </p>
              </div>
              <div className="available">
                  Available?
                  <input type="radio" name="available" id="availableChoice1" value="true"/> <label htmlFor="availableChoice1">Yes</label>
                  <input type="radio" name="available" id="availableChoice2" value="false"/> <label htmlFor="availableChoice2">No</label>
              </div>    
              <p> <input type="submit" value="Post Item"/> </p>
          </form>
      </div>
    );
  }
  
  ReactDOM.render(<CreateListing />, document.getElementById('create-listing-container'));