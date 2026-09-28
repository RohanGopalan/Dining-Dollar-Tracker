from datetime import date

from data import load_data

START_AMOUNT = 452.50
START_DATE = date(2026, 8, 21)
END_DATE = date(2026, 12, 19)

def total_spent(data):
    total = 0

    for transact in data:

        total += transact["amount"]
    
    return total

def calc_stats(data):
    spent = total_spent(data)
    percent_spent = 100 * (spent / START_AMOUNT)

    date_today = date.today()
    
    
    amount_left = START_AMOUNT - spent
    
    
    term_length = (END_DATE - START_DATE).days
    
    
    days_since_start = (date_today - START_DATE).days
    
    days_left = (END_DATE - date_today).days
    
    
    spend_per_week = 7 * (amount_left / days_left)
    
    
    percent_of_sem = 100 * (days_since_start / term_length)

    return spent, amount_left, spend_per_week, percent_spent, percent_of_sem


def get_dates_as_list(data):

    dates = []


    for transact in data:

        full_date = transact["date"]

        year = int(full_date[:4])

        month = int(full_date[5:7])

        day = int(full_date[8:])


        dates.append(date(year,month,day))

    return dates

def get_amnt_spent_as_list(data):
    cumulative_amounts = []
    i = 0
    
    for transact in data:
        if i == 0:
            cumulative_amounts.append(START_AMOUNT - transact["amount"])
        else:
            cumulative_amounts.append(cumulative_amounts[i-1] - transact["amount"])

        i += 1

    return cumulative_amounts

def get_start_amount_from_plan(plan):
    if plan in ["Unlimited", "80B", "50B"]:
        return 267.50
    elif plan == "14":
        return 452.50
    elif plan == "10":
        return 587.50
    elif plan == "7":
        return 320
    else:
        return 0
    
