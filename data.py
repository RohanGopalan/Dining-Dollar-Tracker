import json, os

from calculations import set_start_amount

FILE_NAME = "transactions.json"
DEFAULT_FILE = {
    "start_amount": 0,
    "transactions": []
}

def load_data():

    # error checking if the file exists
    if not os.path.exists(FILE_NAME):
        
        with open(FILE_NAME, "w") as file:
            json.dump(DEFAULT_FILE, file, indent=4)
            print("Created transactions.json file...")
            return DEFAULT_FILE

    else:
        # returns dictionary of start_amount and nested dictionary of transactions
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            set_start_amount(data["start_amount"])
            return data

# sort transactions by date and return as list
# works with key x: x['date'] since it's in ISO format as a string
def load_as_sorted(data):
    return sorted(data["transactions"], key=lambda x: x['date'])

# adds transaction to transactions dictionary and rewrites the file
def add_transact(entry, data):

    data["transactions"].append(entry)


    with open(FILE_NAME, "w") as file:

        json.dump(data, file, indent=4)
        print("Transaction saved!")

    return data

# methods for getting and adding start amounts
def get_start_amount(data):
    return data["start_amount"]

def add_start_amount(amount, data):
    data["start_amount"] = amount
    set_start_amount(amount)

    with open(FILE_NAME, "w") as file:

        json.dump(data, file, indent=4)
        print("Meal plan saved!")
    
    return data

    
