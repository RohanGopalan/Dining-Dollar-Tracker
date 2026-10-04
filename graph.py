import matplotlib.pyplot as plt

import matplotlib.dates as mdates

from calculations import get_dates_for_plotting, get_amnt_spent_as_list, get_start_amount, get_start_end
from data import get_sorted_transactions

def graph_data(data):
    fig, axs = plt.subplots(figsize=(10, 6))

    dates = get_dates_for_plotting(data["dates"])

    # plot date on x axis and amount spent subtracted from start amount on y axis
    axs.plot(dates, get_amnt_spent_as_list(data["amounts_spent"]), marker="o", linestyle="-", color="blue", label="Spending")

    start_end = get_start_end()
    
    start_end_amounts = data["start_amount"], 0

    axs.plot(start_end, start_end_amounts, color="green", linestyle="-", label="Projected Spending")

    dates_interval = round((start_end[1] - start_end[0]).days / 30)

    fig.autofmt_xdate()

    axs.set_xlim(left=start_end[0], right=start_end[1])
    axs.xaxis.set_major_locator(mdates.DayLocator(interval=dates_interval))
    axs.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

    axs.set_ylim(top=data["start_amount"], bottom=0)

    plt.ylabel("Amount Remaining")
    plt.xlabel("Date")
    plt.title("Dining Dollar Usage")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    
