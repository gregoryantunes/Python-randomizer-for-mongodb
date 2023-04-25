import pymongo
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

num_deletes = random.randint(30, 10000)

for i in range(num_deletes):
    query = {"_id": random.choice(list(mycol.find()))["_id"]}
    mycol.delete_one(query) 

print(f"{num_deletes} documents were deleted from the collection.")
