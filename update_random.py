import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

num_updates = random.randint(30, 100) 

for i in range(num_updates):
    name = ''.join(random.choice(string.ascii_letters) for i in range(10))
    address = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))
    filter = {"name": name}
    update = {"$set": {"address": address}}
    mycol.update_one(filter, update)

print(f"{num_updates} documents were updated in the collection.")
