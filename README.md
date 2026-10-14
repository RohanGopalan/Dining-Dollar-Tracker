# Dining Dollar Calc

A simple Python tool to track Purdue Dining Dollar spending throughout the semester.

If you're on a meal plan and want to know how much you’ve spent, how much you have left, and whether you're burning through your Dining Dollars too quickly, this project is for you. Instead of manually tracking everything, just enter your spending and let the program handle the math.

## Features

- **Track spending:** Log Dining Dollar transactions and save them locally.
- **Compare against an ideal budget:** See how much you're ahead of or behind the ideal spending pace based on the time elapsed in the semester.
- **Visualize spending:** Generate a graph comparing your remaining balance against an ideal spending trajectory.
- **Automation and Persistence:** Automatically get and save the semester you're in based on the date, prompt and save the meal plan you're on, and save transactions to a json.

## Built With

- Python
- Matplotlib for plotting
- NumPy for sorting and handling transaction data
- JSON for local data storage

## Getting Started

### Prerequisites

- Python 3
    - `matplotlib`
    - `numpy`

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the dependencies:

   ```bash
   pip install matplotlib numpy
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## Usage

When you run the program, it will guide you through setting up your tracking data if this is your first time using it.

1. **Set your semester:** If you're outside the months August to December or January to May, you can choose a semester to simulate. Otherwise, the program will automatically determine your semester
2. **Select your meal plan:** Choose your Purdue meal plan so the program can save your initial Dining Dollar amount.
3. **Enter a transaction:** Input the amount you just spent. To instead skip right to the statistics, input letters or an invalid number to proceed.
4. **Review your stats:** Check your total spending, remaining balance, budget progress, and recommended weekly spending.
5. **Check the graph:** Once you have transactions on multiple dates, a graph displays your remaining balance over time against the ideal spending line.

### Example Output

```text
You have spent $87.50 so far
You have $365.00 left, which is $25.00 more than optimal by this time
You're 30.0% through the semester and you've spent 19.4% of your budget
You can spend $22.00 per week to stay on track
```

*Example output only. Actual values depend on your meal plan, spending history, and the current date.*

## Meal Plans

The program uses the following Dining Dollar amounts for each mealplan:

| Meal Plan | Starting Balance |
|---|---:|
| Unlimited | $267.50 |
| 14 Track | $452.50 |
| 10 Track | $587.50 |
| 7 Track | $320.00 |
| 80 Block | $267.50 |
| 50 Block | $267.50 |

These values are configured in `calculations.py` and can be updated if the plan amounts change.

## How It Works

The project is split into a few modules, each handling a different part of the program.

| File | Purpose |
|---|---|
| `main.py` | Runs the program, handles user input, and displays statistics. |
| `calculations.py` | Calculates spending statistics, determines semester dates, and manages budget calculations. |
| `data.py` | Bridges JSON file and Python files by using the json library to read and write data. |
| `graph.py` | Generates spending graph using Matplotlib. |
| `transactions.json` | Stores starting balance, semester, transaction amounts, and transaction dates. |

### Data Storage

Your data is stored locally in `transactions.json`. The file uses a dictionary to store your meal plan's starting amount, the current semester, and two corresponding lists for the amount spent and date of a transaction.

For example:

```json
{
    "start_amount": 452.5,
    "semester": "Fall",
    "amounts_spent": [
        8.50,
        12.00,
        5.25
    ],
    "dates": [
        "2026-08-25",
        "2026-08-27",
        "2026-08-29"
    ]
}
```

Each transaction amount corresponds to a date at the same index in the respective lists.

**Note:** Keep a backup of `transactions.json` if you want to preserve your spending history. The program writes updates directly to this file.

## Future Improvements

Some things I'd like to add or improve:

- [ ] Handle continuity between semesters without needing to manually clear transactions and add a starting amount
- [ ] Add the ability to edit or remove previous transactions, likely in a GUI.
- [ ] Improve the graph with additional spending statistics and visualizations.

## Why I Built This

I wanted a simple way to keep track of my Dining Dollars at Purdue without having to do mental math or follow an arbitrary weekly budget. The goal is to know where my budget stands and whether I'm spending too much early in the semester.

It's a small project, but it's also a practical way to work with Python, modular program design, file I/O, date calculations, and data visualization.

---

Built for keeping those Dining Dollars alive until finals.