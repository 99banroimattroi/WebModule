from db import food_collection
from bson import ObjectId

def add(name,price):
    new_food = {
        "Name": name,
        "Price": price,
    }

    food_collection.insert_one(new_food)

def get(query): #filter, limit, skip
    food_list = food_collection.find(query) #many
    return food_list

def get_by_id(id):
    f = food_collection.find_one({"_id": ObjectId(id)})
    return f



#D
def delete_by_id(id):
    food_collection.delete_one({"_id": ObjectId(id)})


#U
def update_by_id(id, name, price):
    query = {"_id": ObjectId(id)}
    updater = {
        "$set": {"Name": name},
        "$set": {"Price": price}
    } # $inc, $dec, $set, $unset 
    food_collection.find_one_and_update(query, updater)



# def find_by_username(username):

if __name__ == "__main__":
    query = {"_id": ObjectId("5c812a493b74ac2cecde0ef9")}
    updater = {"$set": {"Price":  60000} } # $inc, $dec, $set, $unset 
    food_collection.find_one_and_update(query, updater)
    print(*get({}), sep="\n")

    # food_collection.delete_one({"_id": ObjectId("5c812d273b74ac327ca6d417")})
    # f = food_collection.find_one({"_id": ObjectId("5c812d273b74ac327ca6d417")})
    # if f != None: #found
    #     print(f["Name"])
    # else:
    #     print("Not found")


    # while True:
    #     name = input("Enter name: ")
    #     price = int(input("Enter price: "))

    #     add(name,price)
    

    # food_list = food_collection.find( #lazy loading
    #     {
    #         "Price": {"$gt": 24000} 
    #     }  #query 
    # )


    # first_food = food_list[0]
    # print(first_food["Name"])
    # print(first_food["Price"])


    # for food in food_list:
    #     print(food["Name"])
    #     print(food["Price"])


    # for food in food_list:
    #     # if food["Name"] == "Bun Ca":
    #         print(food["Name"])
    #         print(food["Price"])







    
    