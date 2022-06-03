function Signup() {
    return (
      <div id="signup-box">
          <form action="/signup" method="POST">
              <div id="signup-banner" className="signup-form"><h1>Signup:</h1></div>
              <div id="email-label" className="signup-form">Email <input type="text" name="email"/> </div> 
              <div id="password-label" className="signup-form">Password <input type="password" name="password"/></div>
              <div id="signup-submit" className="login-form"><input type="submit" /></div>
              <div id="already" className="login-form">Already have an account? <a href="/login">Login!</a></div>
          </form>
      </div>
    );
  }
  
  ReactDOM.render(<Signup />, document.getElementById('signup-div'));