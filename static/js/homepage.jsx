function Homepage() {
    return (
      <div id="homepage-container">
          <div className="logo">CLOOP</div>
          <p id="subline">(<span className="emphasize">Cl </span>ose the L<span className="emphasize"> oop </span>)</p>
          <div className="container">
            <div id="process-entry">
                <div id="byline">The premiere rental marketplace for clothing and accessories.</div>
                <div id="signup-line"><a href="/signup">Sign Up</a>
                </div>
                <div>Already have an account? <a href="/login">Log In</a></div>
            </div>
          </div>s
      </div>
    );
  }
  
  ReactDOM.render(<Homepage />, document.querySelector('#app'));