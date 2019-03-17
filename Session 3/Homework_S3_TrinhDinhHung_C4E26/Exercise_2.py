from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.c4e
detail = db["posts"]
new_detail = {
    "title": "Đình Hùng",
    "content": "Techkids thật tuyệt vời ! Được học với anh Huy là một điều tuyệt vời",
}
detail.insert_one(new_detail)

client.close()


