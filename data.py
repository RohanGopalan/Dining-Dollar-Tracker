import json, os

FILE_NAME = "transactions.json"

def load_data():


    if not os.path.exists(FILE_NAME):


        print(f"{FILE_NAME} could not be found")


        return []
    


    with open(FILE_NAME, "r") as file:

        return json.load(file)


def load_as_sorted_list(data):
    return sorted(data["transactions"], key=lambda x: x['date'])

def add_transact(entry, data):

    data.append(entry)


    with open(FILE_NAME, "w") as file:


        json.dump(data, file, indent=4)
        print("Transaction saved!")

    return data

def get_start_amount(data):
    return data["start_amount"]

def add_start_amount(amount, data):
    data["start_amount"] = amount

    with open(FILE_NAME, "w") as file:

        json.dump(data, file, indent=4)
        print("Meal plan saved!")
    
    return data

    
