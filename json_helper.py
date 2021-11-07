# Directions:
# Define a function called read_json.
# Given a string representing a file path to a json file,
# this function should open said file and covert its contents into a json object.
# The json object should be returned.

# Note to self, helpful link explaining json.load & json.dump: https://www.section.io/engineering-education/storing-data-in-python-using-json-module/

import json

def read_json():
    file_path = input("Provide a file path: ")
    with open(file_path, 'r') as file_object:
        data = json.load(file_object)
    print(data)

read_json()