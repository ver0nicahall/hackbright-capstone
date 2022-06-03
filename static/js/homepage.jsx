function Homepage() {
    return (
      <div id="homepage-container">
          <h1> Welcome to Cloop!</h1>
              <div><a href="/signup">Sign Up</a></div>
              <div>Already have an account? <a href="/login">Log In</a></div>

      </div>
    );
  }
  
  ReactDOM.render(<Homepage />, document.querySelector('#app'));