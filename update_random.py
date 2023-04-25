import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

num_updates = random.randint(30, 100) # Randomly chooses the number of updates to be performed

for i in range(num_updates):
    name = ''.join(random.choice(string.ascii_letters) for i in range(10)) # Generates a random name with 10 letters
    address = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20)) # Generates a random address with 20 alphanumeric characters
    filter = {"name": name} # Creates a filter to find a document with the randomly generated name
    update = {"$set": {"address": address}} # Creates an update to change the address of the found document
    mycol.update_one(filter, update) # Updates the document in the collection

print(f"{num_updates} documents were updated in the collection.")
