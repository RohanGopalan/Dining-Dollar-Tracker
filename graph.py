import matplotlib.pyplot as plt

import matplotlib.dates as mdates

from calculations import get_dates_as_list, get_amnt_spent_as_list

def graph_data(data):
    fig, ax = plt.subplots()
    
    ax.plot(get_dates_as_list(data), get_amnt_spent_as_list(data), marker="o", linestyle="-")
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))


    fig.autofmt_xdate()

    plt.ylim(bottom=0)
    plt.grid(True)

    plt.show()
    
