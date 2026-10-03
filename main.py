from datetime import date

from calculations import calc_stats, get_start_amount_from_plan, set_semester, total_spent
from data import add_start_amount, add_transact, load_data
from graph import graph_data

import sys


def main():

    # load data to begin with
    data = load_data()
    today_date = date.today()

    if data["semester"]:

        if (today_date.month >= 8 and data["semester"] == "Fall") or (today_date.month <= 5 and data["semester"] == "Spring"):
            set_semester(today_date, semester=data["semester"])
        
        else:
            sys.exit(f"Error: Current date does not match saved semester ({data['semester']}).")

    elif not (result := set_semester(today_date, data=data)):
        print("Error: Current date is not within a semester range.")
        mimic_sem = input("Enter semester to mimic (Fall/Spring/None): ").strip().capitalize()
        
        if mimic_sem.startswith("F"):
            today_date = date(today_date.year, 8, max(today_date.month, 25))
            set_semester(today_date, data=data)

        elif mimic_sem.startswith("S"):
            today_date = date(today_date.year, 1, max(today_date.month, 11))
            set_semester(today_date, data=data)

        else:
            sys.exit("Exiting program...")

    else:
        data = result
    
    # if start amount is 0 (unchanged), 
    # prompt for meal plan and set start amount accordingly
    if data["start_amount"] == 0:
        meal_plan = input("Which meal plan are you on? (Unlimited/14/10/7/80B/50B): ").strip().capitalize()
    
        start = get_start_amount_from_plan(meal_plan)
    
        if start != 0:
            data = add_start_amount(start, data)
        else:
            sys.exit("Invalid Input: Please try again.")
    

    amount = input("How much did you spend? $")

    # if user inputs valid number,
    # add transaction to data and save to file
    try:
        amount = float(amount)
        if amount <= 0 or amount > data["start_amount"] - total_spent(data["amounts_spent"]):
            raise ValueError

        date_today_str = today_date.isoformat()
        
        data = add_transact(data, amount, date_today_str)
    
    except ValueError:
        print("Invalid Input: Skipping to statistics...")

    print()

    # calculate and display statistics
    spent, amount_left, spend_per_week, percent_spent, percent_of_sem = calc_stats(data["amounts_spent"])

    print(f"You have spent ${spent:,.2f} so far")
    print(f"You have ${amount_left:,.2f} left")
    print(f"You're {percent_of_sem:.1f}% through the semester and you've spent {percent_spent:.1f}% of your budget")
    print(f"You can spend ${spend_per_week:.2f} per week to stay on track")

    print()

    # display plot of spending over time only if there are more than one unique dates
    unique_dates = set(data["dates"])

    if len(unique_dates) > 1:
        graph_data(data)

if __name__ == "__main__":
    main()