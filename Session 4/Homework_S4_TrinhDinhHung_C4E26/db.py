from pymongo import MongoClient
from urllib.parse import quote_plus

password = quote_plus("951753!@")

uri = f"mongodb+srv://admin_hung:{password}@hung-c4e26-0zkua.mongodb.net/test?retryWrites=true"

#1.Connect
client = MongoClient(uri)

#2.Get database
db = client.test

#3. get collection
food_collection = db["food"]
user_collection = db["user"]

#4. create new document
# new_food = {
#     "Name": "Bun Cha",
#     "price": "20000"
# }
new_user = {
    "username" :"trinhdinhhung",
    "password": "dinhhung05011999"
} 

#5. Insert new documnet into collection

user_collection.insert_one(new_user)

#6. Close connection
def close():
    client.close()
client.close()