"""CRUD operations."""

from model import db, User, Item, Rental, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

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

def create_rental(order_date, start_date, due_date, rental_total, lender, renter, item):

    rental = Rental(
        order_date = order_date,
        start_date = start_date,
        due_date = due_date,
        rental_total=rental_total,
        lender=lender,
        renter=renter,
        item=item
    )
    return rental

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
