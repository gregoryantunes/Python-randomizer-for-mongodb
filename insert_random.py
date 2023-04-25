import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

num_inserts = random.randint(30, 10000) # Escolhe aleatoriamente o número de inserções a serem realizadas

for i in range(num_inserts):
    name = ''.join(random.choice(string.ascii_letters) for i in range(10)) # Gera um nome aleatório de 10 letras
    address = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20)) # Gera um endereço aleatório de 20 caracteres alfanuméricos
    mycol.insert_one({"name": name, "address": address}) # Insere um documento na coleção com o nome e endereço aleatórios

print(f"{num_inserts} documentos foram inseridos na coleção.")

