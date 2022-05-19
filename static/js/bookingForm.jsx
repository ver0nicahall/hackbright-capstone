function BookingForm() {
  const current = new Date()
  const today = `${current.getFullYear()}-${current.getMonth()+1}-${current.getDate()}`;

    return (
      <div id="booking-form">
          <h3>Book this item:</h3>
          <form action="/book" method="POST">
             <p><label for="start">When would you like to book this item? </label> 
             <input type="date" id="start" name="rental-start" min={today} /> </p>
             <p>How long would you like to keep this item for?
             <select name="num_days" id="num_days" form="num_days-form">
             <option value="1">1</option>
             <option value="2">2</option>
             </select> days
             </p>
              <input type="submit" value="Book Item"></input>
          </form>
      </div>
    );
  }
  
  ReactDOM.render(<BookingForm />, document.getElementById('booking-div'));