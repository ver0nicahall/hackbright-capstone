"""Models for clothing rental app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    #items = list of items a user has
    #lends = list of rentals where user has rented out items 
    #rents = list of rentals where user has borrowed
    #reviews_given = reviews given to others for 
    #reviews_received = reviews for rentals
    #messages_sent
    #messages_received

    def __repr__(self):
        """Show info about user."""
        return f'<User user_id={self.user_id} email={self.email}>'

class Item(db.Model):
    """An item listing on the marketplace."""

    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    item_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    num_likes = db.Column(db.Integer)
    num_views = db.Column(db.Integer)
    street_address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(10))
    deleted = db.Column(db.Boolean, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    #rentals = a list of rentals this item has been associated with
    #reviews = a list of reviews this item is associated with
    #images = a list of images associates with this item 

    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    user = db.relationship("User", backref="items")

    def __repr__(self):
        """Show info about item."""
        return f'<Item item_id={self.item_id} item_name={self.item_name} user_id={self.user_id}>'

class Rental(db.Model):
    """An order placed by a user to rent an item"""

    __tablename__ = "rentals"
    
    rental_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False) #when the rental was made
    start_date = db.Column(db.DateTime, nullable=False) #date the rental is supposed to start
    num_days = db.Column(db.Integer, nullable=False) #number of days to rent the item
    rental_total = db.Column(db.Float, nullable=False)

    #foreign keys
    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))
    lender_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    renter_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    #relationships
    lender = db.relationship("User", foreign_keys=[lender_id], backref="lends")
    renter = db.relationship("User", foreign_keys=[renter_id], backref="rents")
    item = db.relationship("Item", backref="rentals") #item being rented

    def __repr__(self):
        """Show info about rental."""
        return f'<Rental rental_id={self.rental_id} rental_total={self.rental_total} item_id={self.item_id}>'

class Review(db.Model):
    """A rating left on an item."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)

    #foreign keys
    lender_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    renter_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))


    #relationships
    item = db.relationship("Item", backref="reviews")
    lender = db.relationship("User", foreign_keys=[lender_id], backref="reviews_received")
    renter = db.relationship("User", foreign_keys=[renter_id], backref="reviews_left")

    def __repr__(self):
        """Show info about review."""
        return f'<Review review_id={self.review_id} score={self.score} item_id={self.item_id}>'

class Message(db.Model):
    """A text message sent from one user to another."""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, nullable=False)
    #foreign keys
    sender_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    #relationships
    sender = db.relationship("User", foreign_keys=[sender_id], backref="messages_sent")
    receiver = db.relationship("User", foreign_keys=[receiver_id], backref="messages_received")

    def __repr__(self):
        """Show info about message."""
        return f'<Review message_id={self.message_id} text={self.text} timestamp={self.timestamp}>'

class Image(db.Model):
    """An image associated with a listing."""

    __tablename__ = "images"

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    url = db.Column(db.String, nullable=False)
    
    #foreignkey
    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))

    #relationships
    item = db.relationship("Item", backref="images")

    def __repr__(self):
        """Show info about image."""
        return f'<Image image_id={self.image_id} text={self.url} item_id={self.item_id}>'


def connect_to_db(flask_app, db_uri="postgresql:///rentals", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

