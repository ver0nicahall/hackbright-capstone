function Homepage() {
    return (
      <div id="homepage-container">
          <h1>Cloop</h1>
          <div className="container">
            <div id="process-entry">
                <div><a href="/signup">Sign Up</a></div>
                <div>Already have an account? <a href="/login">Log In</a></div>
            </div>
          </div>
      </div>
    );
  }
  
  ReactDOM.render(<Homepage />, document.querySelector('#app'));