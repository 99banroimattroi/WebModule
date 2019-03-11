from Exercise_4 import river_collection


if __name__=="__main__":

    Africa= []
    Africa_list = river_collection.find(
        {
            "continent": {"$eq": "Africa"}
        }
    )
    for i in Africa_list:
        new_list = {
            "name" : i["name"],
            "continent": i["continent"],
            "length": i["length"]
        }
        Africa.append(new_list)


    print(Africa)