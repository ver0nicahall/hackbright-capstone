function Marketplace() {
    return (
      <div>
          <h1>Cloop Marketplace</h1>
          <h2>Navigation</h2>
          <ul>
              <li>Create a listing</li>
              <li>My profile</li>
              <li>My account</li>
          </ul>

          <h2>~items go here~</h2>
          <div id="marketplace-listings"> items container</div>


      </div>
    );
  }
  
  ReactDOM.render(<Marketplace />, document.getElementById('marketplace-container'));