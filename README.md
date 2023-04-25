# Scripts Python para manipulação de dados no MongoDB
Neste repositório, são disponibilizados alguns scripts em Python que utilizam a biblioteca pymongo para manipular dados em um banco de dados MongoDB.

### Pré-requisitos
Para executar os scripts, é necessário ter o Python 3 e a biblioteca pymongo instalados em sua máquina. Além disso, é preciso ter um servidor MongoDB em execução, seja localmente ou em algum serviço de nuvem.

## Script 1: insert_random.py
Este script realiza inserções aleatórias na coleção "customers" do banco de dados "mydatabase". Para cada inserção, um nome aleatório de 10 letras e um endereço aleatório de 20 caracteres alfanuméricos são gerados. O número de inserções a serem realizadas é definido no início do script.

## Script 2: delete_random.py
Este script realiza exclusões aleatórias na coleção "customers" do banco de dados "mydatabase". O número de exclusões a serem realizadas é definido aleatoriamente entre 30 e 10000. Para cada exclusão, é escolhido aleatoriamente um documento na coleção e ele é removido.

## Script 3: update_random.py
Este script realiza atualizações aleatórias na coleção "customers" do banco de dados "mydatabase". O número de atualizações a serem realizadas é definido aleatoriamente entre 30 e 100. Para cada atualização, é escolhido aleatoriamente um documento na coleção e o seu endereço é atualizado para um valor aleatório de 20 caracteres alfanuméricos.

### Como executar
Para executar cada um dos scripts, basta abrir o terminal, navegar até o diretório onde os scripts estão localizados e rodar o comando python <nome_do_script>.py. Certifique-se de ter definido corretamente as informações de conexão ao servidor MongoDB no início de cada script.

---

# Python Scripts for Data Manipulation in MongoDB
In this repository, some Python scripts are available that use the pymongo library to manipulate data in a MongoDB database.

### Prerequisites
To run the scripts, it is necessary to have Python 3 and the pymongo library installed on your machine. Additionally, a MongoDB server must be running, either locally or on some cloud service.

## Script 1: insert_random.py
This script performs random inserts into the "customers" collection of the "mydatabase" database. For each insertion, a random 10-letter name and a random 20-character alphanumeric address are generated. The number of insertions to be performed is defined at the beginning of the script.

## Script 2: delete_random.py
This script performs random deletions in the "customers" collection of the "mydatabase" database. The number of deletions to be performed is randomly defined between 30 and 10000. For each deletion, a document in the collection is randomly chosen and removed.

## Script 3: update_random.py
This script performs random updates in the "customers" collection of the "mydatabase" database. The number of updates to be performed is randomly defined between 30 and 100. For each update, a document in the collection is randomly chosen and its address is updated to a random 20-character alphanumeric value.

### How to run
To run each of the scripts, simply open the terminal, navigate to the directory where the scripts are located, and run the command python <script_name>.py. Make sure to properly define the MongoDB server connection information at the beginning of each script.
