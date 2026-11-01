from datetime import date

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from numpy.polynomial import Polynomial as P

from calculations import get_lists_for_plotting, get_start_end
import calculations as cal


def graph_data(data):

    # initialize matplotlib subplots
    fig, axs = plt.subplots(figsize=(10, 6))
    fig.canvas.manager.set_window_title("Dining Dollar Usage")

    amnt_remaining, dates = get_lists_for_plotting(data)

    # get start and end date objects from calculations.py
    start_end = get_start_end()


    # calculate days since start for each date to be used in spending trendline
    days_since_start = ( dates.astype("datetime64[D]") - np.datetime64(start_end[0]) ).astype(int)

    # creates LSRL of spending anchored at the start amount
    spending_trend = anchored_lsrl(data["start_amount"], days_since_start, amnt_remaining)
    
    # tuple for min and max x values for spending trendline
    days_in_sem = (0, (start_end[1] - start_end[0]).days)

    # plot spending trendline as orange and half opacity
    axs.plot(start_end, spending_trend(days_in_sem), color="#ff7f0e", alpha=0.5, label="Spending Trendline")


    # plot date on x axis and amount spent subtracted from start amount on y axis
    axs.plot(dates, amnt_remaining, marker="o", linestyle="-", color="blue", markersize=4, label="Your Spending")
    

    # tuple of optimal spending amounts from start to finish of semester
    start_end_amounts = data["start_amount"], 0

    # plot optimal spending as 2 points for start and end of semester in green
    axs.plot(start_end, start_end_amounts, color="green", linestyle="-", label="Optimal Spending")


    # plot vertical dotted red line for current date
    axs.axvline(x=date.today(), color='r', linestyle=':', alpha=0.5, label="Current Date")

    # specifies how many days are between each x tick
    # 30 is the number of x ticks
    dates_interval = round((start_end[1] - start_end[0]).days / 30)

    # rotate date labels on x axis so they don't overlap
    fig.autofmt_xdate()

    # format x axis date limits, interval, and naming so it shows up as ex. Oct 30
    axs.set_xlim(left=start_end[0], right=start_end[1])
    axs.xaxis.set_major_locator(mdates.DayLocator(interval=dates_interval))
    axs.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

    # set y axis limits based on start amount
    axs.set_ylim(top=data["start_amount"], bottom=0)

    # label axes, figure, and enable legend and grid
    plt.ylabel("Amount Remaining")
    plt.xlabel("Date")
    plt.title("Dining Dollar Usage")
    plt.legend()
    plt.grid(True)

    # fits plot to full window and shows it
    plt.tight_layout()
    plt.show()
    
def anchored_lsrl(start, x, y):
    m = np.sum(x * (y - start)) / np.sum(x**2)
    b = start

    return P(coef=(b, m))