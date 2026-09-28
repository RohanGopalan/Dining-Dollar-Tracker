from datetime import date

from calculations import calc_stats, get_start_amount_from_plan
from data import add_start_amount, add_transact, get_start_amount, load_as_sorted_list, load_data
from graph import graph_data

import sys


def main():


    data = load_data()
    
    if get_start_amount(data) == 0:
        meal_plan = input("Which meal plan are you on? (Unlimited/14/10/7/80B/50B): ").capitalize()
    
        start = get_start_amount_from_plan(meal_plan)
    
        if start != 0:
            data = add_start_amount(start, data)
        else:
            sys.exit("Invalid Input: Please try again.")
    

    amount = input("How much did you spend? $")    

    if not amount == "s":
        amount = float(amount)
        
        date_today_str = date.today().isoformat()
        
        entry = {
            "amount": amount,
            "date": date_today_str
        }
        data = add_transact(entry, data)
    
    print()


    spent, amount_left, spend_per_week, percent_spent, percent_of_sem = calc_stats(data["transactions"])
    

    print(f"You have spent ${spent:,.2f} so far")


    print(f"You have ${amount_left:,.2f} left")


    print(f"You're {percent_of_sem:.1f}% through the semester and you've spent {percent_spent:.1f}% of your budget")


    print(f"You can spend ${spend_per_week:.2f} per week to stay on track")

    graph_data(data)



if __name__ == "__main__":
    main()


