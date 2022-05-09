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

#create users and generate 10 fake items for each user
for n in range(1, 10):
    email=f'user{n}@test.com'
    password='test{n}'

    #create a user, add to db 
    user = crud.create_user(email, password)
    model.db.session.add(user)

    #for each user, create 5 items?
model.db.session.commit()

#create some fake rentals
    
#commit everything
model.db.session.commit()

