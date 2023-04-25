import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

num_inserts = random.randint(30, 10000)

for i in range(num_inserts):
    name = ''.join(random.choice(string.ascii_letters) for i in range(10)) 
    address = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20)) 
    mydict = {"name": name, "address": address} 
    x = mycol.insert_one(mydict) 

print(f"{num_inserts} documents were inserted into the collection.")
