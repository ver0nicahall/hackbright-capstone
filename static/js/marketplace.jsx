function Marketplace() {
    return (
      <div>
          <h1>Cloop Marketplace</h1>
          <h2>Navigation</h2>
          <ul>
              <li><a href="/create_listing">New Listing</a></li>
              <li>My profile</li>
              <li>My account</li>
              <li>Search for an item:</li>
          </ul>

          <h2>~items go here~</h2>
          <div id="marketplace-listings"> items container</div>


      </div>
    );
  }
  
  ReactDOM.render(<Marketplace />, document.getElementById('marketplace-container'));