import csv
import json
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Define the CSV file path as a variable
csv_file_path = 'C:\\Users\\natty\\Desktop\\cats.csv'

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Extraction
# Open the CSV file for reading
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(csv_file)

# Transformation
# Initialize an empty list to store the JSON data
    data = []

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Update adoption data
        if row['name'] == 'Oreo':
            # Increment the age of Bob by 2
            row['adopted'] = "True"
            row['adoption_date'] = '2023-10-11'
            row['adopters_name'] = 'Christine Johnson'
            print(f"{row['name']} has been adopted!")

        if row['name'] == 'Snickers':
            # Update adoption data
            row['adopted'] = "True"
            row['adoption_date'] = '2023-10-11'
            row['adopters_name'] = 'Erik Williams'
            print(f"{row['name']} has been adopted!")

        if row['name'] == 'Shoyu':
            # Update adoption data
            row['adopted'] = "True"
            row['adoption_date'] = '2023-10-12'
            row['adopters_name'] = 'Jennifer Miller'
            print(f"{row['name']} has been adopted!")

        # Append each row as a dictionary to the data list
        data.append(row)

# Write the data to a JSON file
with open('cats.json', 'w') as json_file:
    # Use the json.dump() function to write the data to the JSON file
    json.dump(data, json_file, indent=4)

print("CSV data has been successfully converted to JSON.")


## Load
# Connect to the MongoDB server
client = MongoClient(MONGODB_URI)

# Access the cat_rescue database
db = client['cat_rescue']

# Access the cats collection
collection = db['cats']

# Open the JSON file for reading
with open('cats.json', 'r') as json_file:
    # Load the JSON data from the file
    data = json.load(json_file)

    # Insert the data into the MongoDB collection
    collection.insert_many(data)

print("Cats data successfully inserted into Cat Rescue Database!")