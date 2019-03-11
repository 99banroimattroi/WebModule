from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.c4e
print("Kết nối thành công")

client.close()
