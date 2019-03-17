from pymongo import MongoClient
from urllib.parse import quote_plus

password = quote_plus("951753!@")

uri = f"mongodb+srv://admin_hung:{password}@hung-c4e26-0zkua.mongodb.net/test?retryWrites=true"

#1.Connect
client = MongoClient(uri)

#2.Get database
db = client.test

#3.Get colllection
food_collection = db["food"]   #collection

# #4.Create a new document
# new_food = {
#     "Name": "Bun Cha",
#     "price": "20000",
# } #document

# #5. Insert new docment into colllection

# food_collection.insert_one(new_food)

#6. Close connection
def close():
    client.close()
client.close()