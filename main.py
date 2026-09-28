from datetime import date
import os

import json

import matplotlib.pyplot as plt

import matplotlib.dates as mdates

from calculations import calc_stats, get_dates_as_list
from data import add_transact, load_as_sorted_list, load_data
from graph import graph_data


def main():


    amount = input("How much did you spend? $")

    date_today = date.today()
    print()


    if not amount == "s":
        amount = float(amount)
        
        date_today_str = date_today.isoformat()
        
        entry = {
            "amount": amount,
            "date": date_today_str
        }
        add_transact(entry)
    
    data = load_data()


    spent, amount_left, spend_per_week, percent_spent, percent_of_sem = calc_stats(data)
    

    print(f"You have spent ${spent:,.2f} so far")


    print(f"You have ${amount_left:,.2f} left")


    print(f"You're {percent_of_sem:.1f}% through the semester and you've spent {percent_spent:.1f}% of your budget")


    print(f"You can spend ${spend_per_week:.2f} per week to stay on track")

    graph_data(load_as_sorted_list(data))



if __name__ == "__main__":
    main()


