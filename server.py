"""Server for online rental marketplace"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud 

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage."""

    #if user is logged in 
    if "user_email" in session:
        #redirect to marketplace
        return redirect("/marketplace")

    return render_template("homepage.html")

@app.route("/signup")
def show_signup():
    """View signup page."""

    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup_user():
    """Signs a user into our database."""

    email = request.form["email"]
    password = request.form["password"]

    #if user with this account already exists:
    if (crud.get_user_by_email(email)):
        flash('Error: An account with that email already exists.')
    else:
        #create user using crud function 
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash('Account created! You may now login.')
    
    #redirect to login page
    return redirect('/login')

@app.route("/login")
def show_login():
   """View login page."""
   
   return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_user():
   """Logs in a user."""
   
   #get email and password from form
   email = request.form["email"]
   password = request.form["password"]

   #retrieve user
   user = crud.get_user_by_email(email)
   
   #if user does not exist or password is in correct
   if not user or user.password != password:
       #flash error message
       flash("The email or password you entered was incorrect.")
       #redirect to login page
       return redirect('/login')
   else:
        #flash success message
        flash('You have successfully been logged in!')
        #set session cookie
        session['user_email'] = email
        #redirect to marketplace
        return redirect('/marketplace')
  
@app.route("/logout")
def logout_user():
    """Logs out a user."""

    session["user_email"] = None
    flash("You've successfully been logged out!")

    return redirect("/")

@app.route("/marketplace")
def view_marketplace():
    """Show marketplace."""
    
    return render_template("marketplace.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
