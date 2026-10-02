import matplotlib.pyplot as plt

import matplotlib.dates as mdates

from calculations import get_dates_as_date_objs, get_amnt_spent_as_list
from data import load_as_sorted

def graph_data(data):
    fig, ax = plt.subplots()
    
    sorted_transactions = load_as_sorted(data)

    # plot date on x axis and amount spent subtracted from start amount on y axis
    ax.plot(get_dates_as_date_objs(sorted_transactions), get_amnt_spent_as_list(sorted_transactions), marker="o", linestyle="-")
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

    # rotates date labels to avoid overlap
    fig.autofmt_xdate()

    plt.ylim(top=data["start_amount"],bottom=0)
    plt.grid(True)

    plt.show()
    
