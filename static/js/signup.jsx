function Signup() {
    return (
      <div>
          <h1>Signup:</h1>
          <form action="/signup" method="POST">
              <p>
                  Email <input type="text" name="email"/>
              </p>
              <p>
                  Password <input type="password" name="password"/>
              </p>
              <p> <input type="submit" /> </p>
          </form>
          <div>Already have an account? <a href="/login">Login!</a></div>

      </div>
    );
  }
  
  ReactDOM.render(<Signup />, document.getElementById('signup-div'));