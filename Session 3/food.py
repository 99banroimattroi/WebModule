from db import food_collection

def add(name,price):
    new_food = {
        "Name": name,
        "Price": price,
    }

    food_collection.insert_one(new_food)

def get():
    food_list = food_collection.find()
    return food_list

if __name__ == "__main__":
    # while True:
    #     name = input("Enter name: ")
    #     price = int(input("Enter price: "))

    #     add(name,price)
    
    food_list = food_collection.find( #lazy loading
        {
            "Price": {"$gt": 24000} 
        }    
    )
    # first_food = food_list[0]
    # print(first_food["Name"])
    # print(first_food["Price"])

    for food in food_list:
        print(food["Name"])
        print(food["Price"])
    
    # for food in food_list:
    #     # if food["Name"] == "Bun Ca":
    #         print(food["Name"])
    #         print(food["Price"])
        





    
    