function CreateListing() {
    return (
      <div>
          <h1>New Listing</h1>
          <form action="/create_listing" method="POST" id="listing-form">
              <h3>Item Info</h3>
              <p>Photos: <form action="/upload-image" method="post" enctype="multipart/form-data">
                  <input type="file" name="my-image"/>
                  <input type="submit"/>
                  </form></p>
              <p>Title <input type="text" name="item_name"/></p>
              <p>Description <textarea name="description" id="listing-form"/></p>
              <div class="price">Price: <input type="text" name="price"/></div>
              <div class="address">
                  <h4>Address</h4>
                  <p>Street address (include unit #): <input type="text" name="street_address"/> </p>
                  <p>City: <input type="text" name="city"/> State: <input type="text" name="state"/> Zipcode: <input type="text" name="zipcode"/> </p>
              </div>
              <div class="available">
                  Available?
                  <input type="radio" name="available" id="availableChoice1" value="true"/> <label for="availableChoice1">Yes</label>
                  <input type="radio" name="available" id="availableChoice2" value="false"/> <label for="availableChoice2">No</label>
              </div>    
              <p> <input type="submit" value="Post Item"/> </p>
          </form>
      </div>
    );
  }
  
  ReactDOM.render(<CreateListing />, document.getElementById('create-listing-container'));