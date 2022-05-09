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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
adjs = ['fancy', 'cute', 'comfy', 'expensive', 'well-loved', 'gala']
articles = ['hat', 'dress', 'shirt', 'jeans', 'skirt', 'overalls', 'onesie', 'costume']


#create users and generate 10 fake items for each user
for n in range(1, 11):
    email=f'user{n}@test.com'
    password='test{n}'

    #create a user, add to db 
    user = crud.create_user(email, password)
    model.db.session.add(user)

    #for each user, create 5 items?
    for n in range (1, 6):

        #create a random name
        name = (choice(colors) + ' ' + choice(adjs) + ' ' + choice(articles))

        item = crud.create_item(name, 'test description', randint(1, 20), 0, 0, '123 main st', 'sunnyvale', 'CA', '94085', True, user)
        #add item to database
        model.db.session.add(item)


model.db.session.commit()

#create some fake rentals


