import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

my_file = "my_file.json"

with open(my_file, 'w') as file_dict:
    json.dump(my_family, file_dict)
   #json.dump(obj2save , destination_file)

with open(my_file, 'r') as a file_dict: