"""Server for online rental marketplace"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db
import crud 
from datetime import datetime

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

#Welcome####################################################################################################

@app.route("/")
def homepage():
    """View homepage."""

    #if user is logged in 
    if "user_email" in session:
        #redirect to marketplace
        return redirect("/marketplace")

    return render_template("homepage.html")

#Login/Signup####################################################################################################

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


#Goodbye####################################################################################################
  
@app.route("/logout")
def logout_user():
    """Logs out a user."""

    session["user_email"] = None
    flash("You've successfully been logged out!")

    return redirect("/")


#View marketplace#############################################################################################

@app.route("/marketplace")
def view_marketplace():
    """Show marketplace."""

    #make sure user is logged in 
    if "user_email" not in session:
        return redirect("/login")

    items = crud.get_all_items()

    return render_template("marketplace.html", items=items)

#Add listing to marketplace######################################################################################

@app.route("/create_listing", methods=["GET", "POST"])
def create_listing():
    """Displays form to create an item listing"""

    #make sure user is logged in
    if "user_email" not in session:
        #redirect to login 
        return redirect("/login")

    if request.method == "GET":
        #show template for creating listing
        return render_template("create_listing.html")
    #for post requests:
    else:
        #fetch data from form
        item_name = request.form["item_name"]
        description = request.form["description"]
        price = int(request.form["price"]) #string to integer
        street_address = request.form["street_address"]
        city = request.form["city"]
        state = request.form["state"]
        zipcode = request.form["zipcode"]
        available = bool(request.form["available"])
        
        #fetch user from session email 
        user = crud.get_user_by_email(session["user_email"])

        #create new listing and add to database
        listing = crud.create_item(
            item_name, description, 
            price, 0, 0,
            street_address,
            city,
            state,
            zipcode,
            available,
            user
        )

        db.session.add(listing)
        db.session.commit()

        #redirect to new listing page - need to change it from marketplace
        return redirect('/marketplace')

#View item###################################################################################

@app.route("/items/<item_id>")
def show_item(item_id):
    """Show details on a particular listing."""

    #retrieve item

    item = crud.get_item_by_id(item_id)

    return render_template("item_details.html", item=item)

#Add booking################################################################################

@app.route("/create_rental")
def create_rental():

    num_days = int(request.form["num_days"])
    renter = crud.get_user_by_email(session["user_email"])
    item = crud.get_item_by_id()
    
    rental = crud.create_rental(
        datetime.date(datetime.now),
        start_date,
        num_days,
        rental_total,
        lender,
        renter,
        item
        )

#View user profile############################################################################

@app.route("/my_profile")
def show_my_profile():
    """Show my profile view."""

    #retrieve own profile using cookie
    user = crud.get_user_by_email(session["user_email"])

    return render_template("user_profile.html", user=user)

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    #retrieve user
    user = crud.get_user_by_id(user_id)

    return render_template("user_profile.html", user=user)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
