function CreateListing() {
    return (
      <div id="new-listing">
          <div className="banner"><h2 className="banner">New Listing</h2></div>
          <form action="/create_listing" method="POST" encType="multipart/form-data" id="listing-form">
            <fieldset>
              <div className="row align-items-center">
                <div className="col-4">
                  <label htmlFor="title">Title:</label>
                  <input type="text" name="item_name" required/>
                </div>

                <div className="col-4">
                  <label htmlFor="price">Price: $</label>
                  <input type="text" name="price" placeholder="(min $1/ max $1000)"required/>
                </div>

                <div className="col-4">
                <label htmlFor="photos">Photos: </label>
                <input type="file" name="listing-image" accept="image/*" required/>
                </div>
              </div>
    
              <div className="row align-items-center">
                <div id="new-description">
                  <label htmlFor="description">Description:</label> 
                  <div><textarea name="description" id="description-textarea" placeholder="Describe your item"/></div>
                </div>
              </div>
              
              <div className ="address">
                  <h3>Location:</h3>
                  <label htmlFor="street-address">Street address (include unit #): </label>
                  <input type="text" name="street_address" required/> 
                  <label htmlFor="city">City:</label><input type="text" name="city" required/> 
                  
                  <label htmlFor="state">State:</label><input type="text" name="state" required/> 
                  <label htmlFor="zipcode">Zipcode:</label><input type="text" name="zipcode" required/>
              </div>

              <div className="available radio">
                  <label htmlFor="available">Available:</label>
                  <input type="radio" name="available" id="availableChoice1" value="true" required/> <label htmlFor="availableChoice1">Yes</label>
                  <input type="radio" name="available" id="availableChoice2" value="false"/> <label htmlFor="availableChoice2">No</label>
              </div> 
              <div id="create-listing-submit"> <input type="submit" value="Post Item"/> </div>
            </fieldset>
          </form>
      </div>
    );
  }
  
  ReactDOM.render(<CreateListing />, document.getElementById('create-listing-container'));