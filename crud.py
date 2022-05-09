"""CRUD operations."""

from model import db, User, Item, Rental, Image, Review, Message, connect_to_db

#users
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

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

#images
def create_image(url, item):

    image = Image(url=url, item=item)

    return image

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
