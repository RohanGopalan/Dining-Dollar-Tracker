from datetime import date

# constant dates for fall semester 2026 and 

START_DATE = date(2026, 8, 21)
END_DATE = date(2026, 12, 19)

# start_amount initialized to 0 but set to correct amount after prompting user
# and dictionary for meal plan -> start amount
START_AMOUNT = 0 # note: not fully constant, but constant when used for calculations
MEAL_PLAN_AMOUNTS = {
    "Unlimited": 267.50,
    "14": 452.50,
    "10": 587.50,
    "7": 320,
    "80": 267.50,
    "50": 267.50,
}

def total_spent(amounts):
    return sum(amounts)

def calc_stats(data):
    # first find percent of money spent
    spent = total_spent(data)
    percent_spent = 100 * (spent / START_AMOUNT)

    date_today = date.today()
    
    
    amount_left = START_AMOUNT - spent
    
    # find term length, days since start, and days left using timedelta
    term_length = (END_DATE - START_DATE).days
    
    
    days_since_start = (date_today - START_DATE).days
    
    days_left = (END_DATE - date_today).days
    
    
    spend_per_week = 7 * (amount_left / days_left)
    
    
    percent_of_sem = 100 * (days_since_start / term_length)

    # return all values as tuple
    return spent, amount_left, spend_per_week, percent_spent, percent_of_sem


# takes in dictionary of transactions (not including start_amount)
def get_dates_as_date_objs(data):

    dates = []

    # loops through transactions and splits date string to create date object for plotting
    for date_current in data:

        year = int(date_current[:4])

        month = int(date_current[5:7])

        day = int(date_current[8:])


        dates.append(date.fromisoformat(date_current))

    return dates

def get_amnt_spent_as_list(data):
    cumulative_amounts = []
    i = 0
    
    # creates list starting with start amount
    # and subtracting each transaction to create cumulative amounts for plotting
    for amount in data:
        if i == 0:
            cumulative_amounts.append(START_AMOUNT - amount)
        else:
            cumulative_amounts.append(cumulative_amounts[i-1] - amount)

        i += 1

    return cumulative_amounts

# methods to get start amount from meal plan and set it
def get_start_amount_from_plan(plan):
    # loop through meal plan dictionary and check if user input is contained by any keys or starts with any keys
    # this allows user to input "unl" for "unlimited" or "14 track" for "14" and have it work
    for meal_plan, amount in MEAL_PLAN_AMOUNTS.items():
        if plan in meal_plan or plan.startswith(meal_plan):
            return amount
    return 0

def set_start_amount(amount):
    global START_AMOUNT
    START_AMOUNT = amount
