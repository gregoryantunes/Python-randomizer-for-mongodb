import pymongo
import random
import string

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

num_updates = random.randint(30, 100) # Escolhe aleatoriamente o número de updates a serem realizados

for i in range(num_updates):
    name = ''.join(random.choice(string.ascii_letters) for i in range(10)) # Gera um nome aleatório de 10 letras
    address = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20)) # Gera um endereço aleatório de 20 caracteres alfanuméricos
    filter = {"name": name} # Cria um filtro para encontrar um documento com o nome gerado aleatoriamente
    update = {"$set": {"address": address}} # Cria um update para alterar o endereço do documento encontrado
    mycol.update_one(filter, update) # Atualiza o documento na coleção

print(f"{num_updates} documentos foram atualizados na coleção.")

