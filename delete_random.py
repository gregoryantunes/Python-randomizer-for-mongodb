import pymongo
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

count = mycol.count_documents({}) # Obtém o número de documentos na coleção
num_to_delete = random.randint(30, 10000) # Escolhe aleatoriamente o número de documentos a serem excluídos
if num_to_delete >= count:
    print("Não há documentos suficientes na coleção para excluir.")
else:
    random_docs = random.sample(range(0, count), num_to_delete) # Escolhe aleatoriamente os índices dos documentos a serem excluídos
    docs_to_delete = [mycol.find()[i] for i in random_docs] # Obtém os documentos correspondentes aos índices escolhidos
    for doc in docs_to_delete:
        mycol.delete_one(doc) # Exclui cada documento
    print(f"{num_to_delete} documentos foram excluídos da coleção.")

