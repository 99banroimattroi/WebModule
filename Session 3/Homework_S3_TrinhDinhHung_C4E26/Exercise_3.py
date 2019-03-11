from Exercise_2 import db
from pymongo import MongoClient
import matplotlib.pyplot as plt

customers_collection = db["customers"]

customers_list = customers_collection.find()

ev = 0
wom = 0
ads = 0
for c in customers_list:
    if (c["ref"]=="events"):
        ev+=1
    elif (c["ref"]=="wom"):
        wom +=1
    elif (c["ref"]=="ads"): 
        ads +=1

sizes = [ev,wom,ads]
labels = 'events', 'wom', 'ads'
colors = ['red', 'gold', 'green']

plt.pie(
    sizes, 
    labels=labels, 
    colors=colors,
    autopct='%1.1f%%',
    startangle=150
)
 
plt.axis("equal")
plt.show()