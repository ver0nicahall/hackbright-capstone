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


      </div>
    );
  }
  
  ReactDOM.render(<Signup />, document.getElementById('signup-div'));