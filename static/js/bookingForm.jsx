function BookingForm() {
    return (
      <div id="booking-form">
          <h3>Book this item:</h3>
          <form action="/book" method="POST">
             <p>When would you like to book this item? ((date)) </p>
             <p>How long would you like to keep this item for?
             <select name="num_days" id="num_days" form="num_days-form">
             <option value="1">1</option>
             <option value="2">2</option>

             </select>
             </p>
              <input type="submit"></input>
          </form>
      </div>
    );
  }
  
  ReactDOM.render(<BookingForm />, document.getElementById('booking-div'));