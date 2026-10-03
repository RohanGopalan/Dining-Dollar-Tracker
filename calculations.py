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

# dictionary for semester to args for term start and end dates
SEMESTER_DATES = {
    "Fall": ((4, "Monday", 8), (3, "Saturday", 12)),
    "Spring": ((2, "Monday", 1), (2, "Saturday", 5))
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

    # if semester is not explicitly given, determine it from month
    if semester is None:
        month = today_date.month

        if month >= 8:
            semester = "Fall"
        elif month <= 5:
            semester = "Spring"
        else:
            return None

    # set dates for semester
    START_DATE, END_DATE = get_semester_dates(semester, today_date.year)

    if START_DATE is None or END_DATE is None:
        return None

    # if data is given (meaning semester is being set for the first time), add it to json and return data to main
    if data is not None:
        data = add_semester(semester, data)
        return data

def get_semester_dates(semester, year):
    if semester not in SEMESTER_DATES:
        return None

    # use dictionary to get args nth_weekday function for start and end dates
    start, end = SEMESTER_DATES[semester]

    # unpack start and end args into get_nth_weekday function to get dates
    start_date = get_nth_weekday(*start, year)
    end_date = get_nth_weekday(*end, year)

    return start_date, end_date

# mathematically return the date object for nth weekday of a given month and year
def get_nth_weekday(n, weekday, month, year):
    weekday_int = WEEKDAY_TO_INT.get(weekday.capitalize(), 0)

    first_day = date(year, month, 1)
    first_weekday = first_day.weekday()

    day = 1 + (weekday_int - first_weekday) % 7 + 7 * (n - 1)

    return date(year, month, day)