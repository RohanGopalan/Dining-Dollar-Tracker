import json, os

FILE_NAME = "transactions.json"

def load_data():


    if not os.path.exists(FILE_NAME):


        print(f"{FILE_NAME} could not be found")


        return []
    


    with open(FILE_NAME, "r") as file:

        return json.load(file)


def load_as_sorted_list(data):
    return sorted(data, key=lambda x: x['date'])

def add_transact(entry):


    current_data = load_data()



    current_data.append(entry)



    with open(FILE_NAME, "w") as file:


        json.dump(current_data, file, indent=4)


        print("Transaction saved!")
