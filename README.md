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
