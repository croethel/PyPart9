import json
import os
import pickle

# Part A Directions:
    # Define a function called read_json.
    # Given a string representing a file path to a json file,
    # this function should open said file and covert its contents into a json object.
    # The json object should be returned.
    # Part A test: read_json(/Users/roethelchristine/dev/PyPart9/data/super_smash_bros/link.json)

def read_json(filepath):
    with open(filepath, 'r') as file_object:
        data = json.load(file_object)
    return data

# Part B Directions:
    # Define a function called read_all_json_files.
    # Given a string representing a path to a directory,
    # this function should read all of the json files
    # and return a list containing all of the json objects.
    # Make sure to incorporate the work from part A.
    # Part B test: read_all_json_files('/Users/roethelchristine/dev/PyPart9/data/super_smash_bros/')

def read_all_json_files(directory):
    json_list = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith('.json'):
                data = read_json(os.path.join(directory, f))
                json_list.append(data)
    return json_list


# Part C Directions:
    # Define a function called write_pickle.
    # This function should take a file path and some data.
    # Given these parameters, the function should write the contents of the json files
    # to a file called super_smash_characters.pickle.
    #Test Part C: write_pickle('/Users/roethelchristine/dev/PyPart9/data/super_smash_bros/link.json', 'super_smash_characters')

def write_pickle(filepath, data):
    data_content = read_json(filepath)
    with open(f'{data}.pickle', 'wb') as pickle_file:
        pickle.dump(data_content, pickle_file)


# Part Part D Directions:
    # Define a function called load_pickle.
    # Given a file path, this function opens a pickled file and returns the data.
    # Use this function to print the pickled data from Part C to the screen.
    #Part D Test write_pickle('/Users/roethelchristine/dev/PyPart9/data/super_smash_bros/link.json', 'super_smash_characters')
    #Part D Test load_pickle('super_smash_characters')

def load_pickle(picklefilepath):
    with open(f'{picklefilepath}.pickle', 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    print(data)




#Exercise 2

data = {
    "name": "Wolverine",
    "neutral_special": "Bone Claw",
    "side_special": "Healing",
    "up_special": "Super Claw Attack",
    "down_special": "Leap Attack",
    "final_smash": "Wolverine Finale"
}

with open('data/marvel/wolverine.json', 'w') as newfile:
    json.dump (data, newfile)
