import json, os
import numpy as np
from calculations import set_start_amount

FILE_NAME = "transactions.json"
DEFAULT_FILE = {
    "start_amount": 0,
    "amounts_spent": [],
    "dates": [],
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
def get_sorted_transactions(data):
    dates = np.asarray(data["dates"])
    amounts = np.asarray(data["amounts_spent"])
    indices = np.argsort(dates.astype("datetime64[D]"))
    return dates[indices], amounts[indices]

# adds transaction to transactions dictionary and rewrites the file
def add_transact(data, amount, date_today):

    data["amounts_spent"].append(amount)
    data["dates"].append(date_today)


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

    
