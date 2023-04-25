import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

num_inserts = random.randint(30, 10000) # Randomly chooses the number of inserts to be performed

for i in range(num_inserts):
    name = ''.join(random.choice(string.ascii_letters) for i in range(10)) # Generates a random name with 10 letters
    address = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20)) # Generates a random address with 20 alphanumeric characters
    mydict = {"name": name, "address": address} # Creates a dictionary with the name and address
    x = mycol.insert_one(mydict) # Inserts the document into the collection

print(f"{num_inserts} documents were inserted into the collection.")
