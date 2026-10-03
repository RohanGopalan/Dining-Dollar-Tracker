from datetime import date

from data import add_semester

START_DATE, END_DATE = None, None

# dictionary for meal plan -> start amount
START_AMOUNT = 0 # note: initialized correctly when loaded from json data
MEAL_PLAN_AMOUNTS = {
    "Unlimited": 267.50,
    "14": 452.50,
    "10": 587.50,
    "7": 320,
    "80": 267.50,
    "50": 267.50,
}

# dictionary to convert weekday string to integer to avoid magic numbers
WEEKDAY_TO_INT = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
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

def set_semester(today_date, semester=None, data=None):
    global START_DATE, END_DATE

    if semester is not None:

        if semester == "Fall":
            START_DATE = get_nth_weekday(4, "Monday", 8, today_date.year)
            END_DATE = get_nth_weekday(3, "Saturday", 12, today_date.year)
            
        elif semester == "Spring":
            START_DATE = get_nth_weekday(2, "Monday", 1, today_date.year)
            END_DATE = get_nth_weekday(2, "Saturday", 5, today_date.year)

        else:
            return False
        
        return True


    if (today_date.month >= 8):
        # find dates for 4th Monday of August and 3rd Saturday of December
        START_DATE = get_nth_weekday(4, "Monday", 8, today_date.year)
        END_DATE = get_nth_weekday(3, "Saturday", 12, today_date.year)

        data = add_semester("Fall", data)
        print("Current semester set to: Fall")
        return data

    elif (today_date.month <= 5):
        # find dates for 2nd Monday of January and 2nd Saturday of May
        START_DATE = get_nth_weekday(2, "Monday", 1, today_date.year)
        END_DATE = get_nth_weekday(2, "Saturday", 5, today_date.year)
        
        data = add_semester("Spring", data)
        print("Current semester set to: Spring")
        return data

    else:
        return False

# mathematically return the date object for nth weekday of a given month and year
def get_nth_weekday(n, weekday, month, year):
    weekday_int = WEEKDAY_TO_INT.get(weekday.capitalize(), 0)

    first_day = date(year, month, 1)
    first_weekday = first_day.weekday()

    day = 1 + (weekday_int - first_weekday) % 7 + 7 * (n - 1)

    return date(year, month, day)