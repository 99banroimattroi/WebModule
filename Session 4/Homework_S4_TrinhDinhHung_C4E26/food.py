from db import food_collection, user_collection
from bson import ObjectId

def add_food(name,price):
    new_food = {
        "Name": name,
        "Price": price,
    }

    food_collection.insert_one(new_food)

def get(query): 
    food_list = food_collection.find(query) 
    return food_list

def get_by_id(id):
    f = food_collection.find_one({"_id": ObjectId(id)})
    return f

def delete_by_id(id):
    food_collection.delete_one({"_id": ObjectId(id)})

def update_by_id(id, name, price):
    query = {"_id": ObjectId(id)}
    updater = {
        "$set": {"Name": name},
        "$set": {"Price": price}
    } # $inc, $dec, $set, $unset 
    food_collection.find_one_and_update(query, updater)

def find_by_username(username):
    tk = user_collection.find_one({"username":username})
    return tk



    