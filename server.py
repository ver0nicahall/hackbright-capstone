"""Server for online clothing rental marketplace"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db, db
import crud 
import os
import cloudinary.uploader
from datetime import datetime

from jinja2 import StrictUndefined

#cloudinary keys
CLOUDINARY_KEY = os.environ["CLOUDINARY_KEY"]
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "cloop"

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


@app.route("/signup", methods=["GET", "POST"])
def signup_user():
    """Signs a user into our database."""

    if request.method == "GET":
        return render_template("signup.html")
    else: 
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


@app.route("/login", methods=["GET", "POST"])
def login_user():
   """Logs in a user."""

   if request.method == "GET":
       return render_template("login.html")
   else:
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

    session.clear()
    flash("You've successfully been logged out!")

    return redirect("/")


#View marketplace#############################################################################################

@app.route("/marketplace")
def view_marketplace():
    """Show marketplace."""

    #make sure user is logged in 
    if "user_email" not in session:
        #redirect user to login page
        return redirect("/login")

    #rertrieve all items from database 
    items = crud.get_all_items()

    #render
    return render_template("marketplace.html", items=items)

@app.route("/api/all_items")
def get_all_listings():
    """Return all listings as JSON."""

    items = crud.get_all_items()
    itemsJSON = []

    #parse each item into a json object
    for item in items:
        item_images = []
        for image in item.images:
            item_images.append(image.url)
        itemJSON = {
            'item_id': item.item_id,
            'item_name': item.item_name,
            'description': item.description,
            'price': item.price,
            'num_likes': item.num_likes,
            'num_views': item.num_views,
            'street_address': item.street_address,
            'city': item.city,
            'state': item.state,
            'zipcode': item.zipcode,
            'deleted': item.deleted,
            'available': item.available,
            'item_images': item_images
        }
        itemsJSON.append(itemJSON)
    
    #return json
    return jsonify(itemsJSON)

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
        deleted = False
        available = bool(request.form["available"])
        #get form data for image
        image_file = request.files["listing-image"]

        #make cloudinary API request:
        result = cloudinary.uploader.upload(
            image_file, 
            api_key=CLOUDINARY_KEY,
            api_secret=CLOUDINARY_SECRET,
            cloud_name = CLOUD_NAME)

        url = result['secure_url']
        
        #fetch user from session email 
        user = crud.get_user_by_email(session["user_email"])

        #create new listing and add to database
        item = crud.create_item(
            item_name, description, 
            price, 0, 0,
            street_address,
            city,
            state,
            zipcode,
            deleted,
            available,
            user
        )

        #create an image and add to database
        image = crud.create_image(url, item)


        db.session.add(item)
        db.session.commit()

        db.session.add(image)
        db.session.commit()

        #fetch new item id, redirect to url
        item_id = item.item_id

        #redirect to new listing page - need to change it from marketplace
        return redirect(f'/items/{item_id}')

#View item###################################################################################

@app.route("/items/<item_id>")
def show_item(item_id):
    """Show details on a particular listing."""

    #retrieve item
    item = crud.get_item_by_id(item_id)

    #prevent user from accessing deleted item
    if item.deleted == True:
        flash('Uh oh! That item is no longer available.')
        #redirect them back to the marketplace
        return redirect('/marketplace')

    return render_template("item_details.html", item=item)

@app.route("/api/items/<item_id>")
def show_itemJSON(item_id):
    """Show details on a particular listing as JSON. """

    #retrieve item
    item = crud.get_item_by_id(item_id)
    item_images = []
    for image in item.images:
        item_images.append(image.url)

    itemJSON = {
        'item_id': item.item_id,
        'item_name': item.item_name,
        'description': item.description,
        'price': item.price,
        'num_likes': item.num_likes,
        'num_views': item.num_views,
        'street_address': item.street_address,
        'city': item.city,
        'state': item.state,
        'zipcode': item.zipcode,
        'deleted': item.deleted,
        'available': item.available,
        'item_images': item_images
    }

    return jsonify(itemJSON)


#Delete Item#################################################################################
@app.route("/items/<item_id>", methods=["POST", "PATCH"])
def delete_item(item_id):
    """Edit or update a particular listing."""
    if request.method == "POST":
        #retrieve item
        crud.delete_item_by_id(item_id)
        flash('Your item has been succesfully deleted!')

        #redirect to marketplace
        return redirect('/marketplace')
    if request.method == "PATCH":
        #retrieve item to be edited
        item = crud.get_item_by_id(item_id)

        #get form inputs, update items
        item.item_name = request.json.get("itemName")
        item.description = request.json.get("description")
        item.price = int(request.json.get("price"))
        item.city = request.json.get("city")
        item.state = request.json.get("state")
        item.zipcode = request.json.get("zipcode")

        db.session.add(item)
        db.session.commit()
        
        return jsonify({
            'item_name': item.item_name,
            'description': item.description,
            'price': item.price,
            'city': item.city,
            'state': item.state,
            'zipcode': item.zipcode,
        })
#Add booking################################################################################

@app.route("/my_rentals")
def view_rentals():
    """Show all of a user's previous rentals"""

    rentals = crud.get_rentals_by_user(session["user_email"])

    return render_template("my_rentals.html", rentals=rentals)

# @app.route("/create_rental")
# def create_rental():

#     num_days = int(request.form["num_days"])
#     renter = crud.get_user_by_email(session["user_email"])
#     item = crud.get_item_by_id()

#     rental = crud.create_rental(
#         datetime.date(datetime.now),
#         start_date,
#         num_days,
#         rental_total,
#         lender,
#         renter,
#         item
#         )

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

@app.route("/api/users/<user_id>/items")
def show_user_items(user_id):
    """Show all items a particular user has as JSON."""

    #retrieve user
    user = crud.get_user_by_id(user_id)
    items = crud.get_items_by_user(user.email)
    itemsJSON = []

   #parse each item into a json object
    for item in items:
        item_images = []
        for image in item.images:
            item_images.append(image.url)
        itemJSON = {
            'item_id': item.item_id,
            'item_name': item.item_name,
            'description': item.description,
            'price': item.price,
            'num_likes': item.num_likes,
            'num_views': item.num_views,
            'street_address': item.street_address,
            'city': item.city,
            'state': item.state,
            'zipcode': item.zipcode,
            'deleted': item.deleted,
            'available': item.available,
            'item_images': item_images
        }
        itemsJSON.append(itemJSON, user=user)
        
    #return json
    return jsonify(itemsJSON)

#Messages###################################################################################
@app.route("/my_messages")
def show_messages():
    """Show messages of logged in user."""
    user = crud.get_user_by_email(session["user_email"])

    return render_template("my_messages.html", user=user)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
