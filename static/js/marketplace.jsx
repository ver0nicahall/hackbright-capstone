function Marketplace() {
    return (
      <div>
          <h1>Cloop Marketplace</h1>
          <h2>Navigation</h2>
          <ul>
              <li><a href="/create_listing">New Listing</a></li>
              <li><a href="/my_profile">My Profile</a></li>
              <li>My Account</li>
              <li>Search for an item: <input type="text"></input> </li> 
          </ul>

          <h2>~items go here~</h2>
      </div>
    );
  }
  
  ReactDOM.render(<Marketplace />, document.getElementById('marketplace-container'));