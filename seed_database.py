"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model 
import server

os.system("dropdb rentals")
os.system("createdb rentals")

#create tables
model.connect_to_db(server.app)
model.db.create_all()

#random generation of clothing
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
adjs = ['fancy', 'cute', 'comfy', 'expensive', 'well-loved', 'gala']
articles = ['hat', 'dress', 'shirt', 'jeans', 'skirt', 'overalls', 'leather jacket', 'heels']

#lists to use later
users_in_db = []
items_in_db = []

#create users and generate 10 fake items for each user
for n in range(1, 11):
    
    email=f'user{n}@test.com'
    password=f'test{n}'

    #create a user
    user = crud.create_user(email, password)
    #add user to database
    users_in_db.append(user)
    # model.db.session.add(user)

    #for each user, create 5 items
    for n in range (1, 6):

        #create a random name
        name = (choice(colors) + ' ' + choice(adjs) + ' ' + choice(articles))

        item = crud.create_item(name, 'test description', randint(1, 20), 0, 0, '123 main st', 'sunnyvale', 'CA', '94085', False, True, user)

        #for each item, create 2 imagess
        for n in range (1, 2):
            if "dress" in item.item_name:
                image = crud.create_image('/static/images/samples/dress.jpeg', item)
            elif "shirt" in item.item_name:
                image = crud.create_image('/static/images/samples/shirt.jpeg', item)
            elif "hat" in item.item_name:
                image = crud.create_image('/static/images/samples/hat.jpeg', item)
            elif "skirt" in item.item_name:
                image = crud.create_image('/static/images/samples/skirt.jpeg', item)
            elif "overalls" in item.item_name:
                image = crud.create_image('/static/images/samples/overalls.jpeg', item)
            elif "jeans" in item.item_name:
                image = crud.create_image('/static/images/samples/jeans.jpeg', item)
            elif "leather" in item.item_name:
                image = crud.create_image('/static/images/samples/leather.jpeg', item)
            elif "heels" in item.item_name:
                image = crud.create_image('/static/images/samples/heels.jpeg', item)
            else: 
                image = crud.create_image('https://dodo.ac/np/images/thumb/8/80/Mabel_NH.png/150px-Mabel_NH.png', item) #placeholder image
            #add images to database
            model.db.session.add(image)

        #add item to database
        items_in_db.append(item)
        # model.db.session.add(item)


model.db.session.add_all(users_in_db)
model.db.session.add_all(items_in_db)
model.db.session.commit()

#create 10 fake rental records
for n in range(1, 11):
    random_item = choice(items_in_db)
    random_lender = choice(users_in_db)
    random_renter = choice(users_in_db)

    #dates
    order_date = datetime.strptime("2022-05-01", "%Y-%m-%d")
    start_date = datetime.strptime("2022-05-02", "%Y-%m-%d")
    num_days = randint(1, 20)
    rental_total = (random_item.price * num_days)

    rental = crud.create_rental(order_date, start_date, num_days, rental_total, random_lender, random_renter, random_item)
    model.db.session.add(rental)

model.db.session.commit()