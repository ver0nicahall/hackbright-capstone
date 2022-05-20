"""CRUD operations."""

from model import db, User, Item, Rental, Image, Review, Message, connect_to_db
from sqlalchemy import update, delete

#users
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_user_by_email(email):
    """Return a single user."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a single user by id."""

    return User.query.get(user_id)


#items

def create_item(item_name, description, price, num_likes, num_views, street_address, city, state, zipcode, available, user):
    """Create and return a new item listing."""

    item = Item(
        item_name=item_name,
        description=description,
        price=price,
        num_likes=num_likes,
        num_views=num_views,
        street_address=street_address,
        city=city,
        state=state,
        zipcode=zipcode,
        available=available,
        user=user
    )
    return item

def get_all_items():
    """Returns all items in database."""

    return Item.query.all()

def get_items_by_user(email):
    """Returns all items owned by user."""

    #find user
    user = User.query.filter(User.email == email).first()

    return Item.query,filter(Item.user_id == user.id)

def get_item_by_id(item_id):
    """Returns all items in database,"""

    return Item.query.get(item_id)

#update function here
def update_item_by_id(item_id):
    pass

def delete_item_by_id(item_id):
    """Deletes an item from database based on id. """

    item_to_delete = Item.query.get(item_id)
    db.session.delete(item_to_delete)
    db.session.commit()


#rentals 
def create_rental(order_date, start_date, num_days, rental_total, lender, renter, item):

    rental = Rental(
        order_date = order_date,
        start_date = start_date,
        num_days = num_days,
        rental_total=rental_total,
        lender=lender,
        renter=renter,
        item=item
    )
    return rental

def get_rentals_by_user(email):
    """Gets all rentals a user has made."""

    user = User.query.filter(User.email == email).first()
    return Rental.query.filter(Rental.renter_id == user.user_id)

#images
def create_image(url, item):

    image = Image(url=url, item=item)

    return image

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
