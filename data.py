import json, os
import numpy as np

FILE_NAME = "transactions.json"
DEFAULT_FILE = {
    "start_amount": 0,
    "semester": "",
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
        from calculations import set_start_amount
        
        # returns dictionary of start amount, lists of dates, and list of amounts spent
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            set_start_amount(data["start_amount"])
            return data

# sort transactions by date and return as list
# TODO sorting is unnecessary bc data is appended chronologically
def get_sorted_transactions(data):
    dates = np.asarray(data["dates"])
    amounts = np.asarray(data["amounts_spent"])
    indices = np.argsort(dates.astype("datetime64[D]"))
    return dates[indices], amounts[indices]

# adds amount spent and date to data dictionary, then rewrites file
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
    
    from calculations import set_start_amount
    set_start_amount(amount)

    with open(FILE_NAME, "w") as file:

        json.dump(data, file, indent=4)
        print("Meal plan saved!")
    
    return data

def add_semester(semester, data):
    data["semester"] = semester.capitalize()

    with open(FILE_NAME, "w") as file:

        json.dump(data, file, indent=4)
        print("Semester saved!")

    return data