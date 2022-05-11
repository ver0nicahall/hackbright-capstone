function Login() {
    return (
      <div>
          <h1>Login:</h1>
          <form action="/login" method="POST">
              <p>
                  Email <input type="text" name="email"/>
              </p>
              <p>
                  Password <input type="password" name="password"/>
              </p>
              <p> <input type="submit" /> </p>
          </form>


      </div>
    );
  }
  
  ReactDOM.render(<Login />, document.getElementById('login-div'));