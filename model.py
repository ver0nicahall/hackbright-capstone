"""Models for clothing rental app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    address = db.Column(db.String)

    def __repr__(self):
        """Show info about user."""
        return f'<User user_id={self.user_id} email={self.email}>'

class Item(db.Model):
    """An item listing on the marketplace."""

    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    item_name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zipcode = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", backref="items")

    def __repr__(self):
        """Show info about item."""
        return f'<Item user_id={self.item_id} item_name={self.item_name}>'

# class Rental(db.Model):
#     """An order placed by a user to rent an item"""

#     __tablename__ = "rentals"
    
#     rental_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     order_date = db.Column(db.DateTime)
#     start_date = db.Column(db.DateTime)
#     due_date = db.Column(db.DateTime)
#     rental_total = db.Column(db.Float)

#     #foreign keys
#     item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"))
#     lender_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
#     renter_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

#     lender = db.relationship("User", backref="rentals")
#     renter = db.Column("User", backref="rentals")
#     item = db.relationship("Item", backref="rentals")

#     def __repr__(self):
#         """Show info about rental."""
#         return f'<Rental lender_id={self.lender_id} renter_id={self.rental_id} rental_total={self.rental_total}>'


def connect_to_db(flask_app, db_uri="postgresql:[///rentals]", echo=True):
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

