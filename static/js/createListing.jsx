function CreateListing() {
    return (
      <div id="new-listing">
          <div className="banner">New Listing</div>
          <form action="/create_listing" method="POST" encType="multipart/form-data" id="listing-form">
            <fieldset>
              <label htmlFor="photos">Photos: </label>
                  <input type="file" name="listing-image" accept="image/*" required/>

              <label htmlFor="title">Title:</label>
              <input type="text" name="item_name" required/>

              <label htmlFor="description">Description</label> 
              <textarea name="description" id="listing-form" placeholder="Describe your item"/>
              
              <label htmlFor="price">Price: </label>
              <input type="text" name="price" required/>
              
              <div className ="address">
                  <h4>Where is this item located?</h4>
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
              <p> <input type="submit" value="Post Item"/> </p>
            </fieldset>
          </form>
      </div>
    );
  }
  
  ReactDOM.render(<CreateListing />, document.getElementById('create-listing-container'));