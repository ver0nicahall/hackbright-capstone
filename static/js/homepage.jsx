function Homepage() {
    return (
      <div>
          <h1> Welcome to Cloop!</h1>
          <ul>
              <li><a href="/signup">Sign Up</a></li>
              <li> Already have an account? <a href="/login">Log In</a></li>
          </ul>
      </div>
    );
  }
  
  ReactDOM.render(<Homepage />, document.querySelector('#app'));