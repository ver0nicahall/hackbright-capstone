function Login() {
    return (
      <div id="login-box">
        <form action="/login" method="POST">
            <div id="login-banner" className="login-form"><h1>CLOOP</h1></div>
            <div id="email-label" className="login-form"> Email <input type="text" name="email"/> </div>
            <div id ="password-label" className="login-form"> Password <input type="password" name="password"/></div>
            <div id="login-submit" className="login-form"><input value="Log In" type="submit" /></div>
            <div id="join-us" className="login-form">No account yet? <a href="/signup">Join us!</a></div>
        </form>
      </div>
    );
  }
  
  ReactDOM.render(<Login />, document.getElementById('login-div'));
