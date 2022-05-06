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
    #lender = 
    #renter =

    def __repr__(self):
        """Show info about user."""
        return f'<User user_id={self.user_id} email={self.email}>'

class Item(db.Model):
    """An item listing on the marketplace."""

    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    item_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(400), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    street_address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(10))

    #rentals = a list of rentals this item has been associated with

    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    user = db.relationship("User", backref="items")

    def __repr__(self):
        """Show info about item."""
        return f'<Item user_id={self.item_id} item_name={self.item_name} user_id={self.user}>'

class Rental(db.Model):
    """An order placed by a user to rent an item"""

    __tablename__ = "rentals"
    
    rental_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False) #when the rental was made
    start_date = db.Column(db.DateTime, nullable=False) #date the rental is supposed to start
    due_date = db.Column(db.DateTime, nullable=False) #date the rental needs to be returned
    rental_total = db.Column(db.Float, nullable=False)

    #foreign keys
    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))
    lender_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    renter_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    #relationships
    lender = db.relationship("User", foreign_keys=[lender_id], backref="rentals")
    renter = db.relationship("User", foreign_keys=[renter_id], backref="rentals")
    item = db.relationship("Item", backref="rentals")

    def __repr__(self):
        """Show info about rental."""
        return f'<Rental lender_id={self.lender_id} renter_id={self.rental_id} rental_total={self.rental_total}>'


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

