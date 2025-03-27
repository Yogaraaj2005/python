#As a college student, you want to keep track of your monthly expenses for better financial management. You categorize expenses into food, rent, utilities, and entertainment. You need a module that does the following: 

import csv
import matplotlib.pyplot as plt

FILENAME = "monthly_expenses.csv"

def save_expenses():
    months = int(input("Enter number of months: "))
    categories = ["Food", "Rent", "Utilities", "Entertainment"]

    with open(FILENAME, "w", newline="") as file:  # Always creates a new file
        writer = csv.writer(file)
        writer.writerow(["Month"] + categories)  # Header

        for month in range(1, months + 1):
            expenses = [input(f"{cat} in Month {month}: ") for cat in categories]
            writer.writerow([f"Month {month}"] + expenses)

def analyze_expenses():
    with open(FILENAME, "r") as file:
        reader = list(csv.reader(file))
        categories = reader[0][1:]
        totals = {cat: 0 for cat in categories}

        for row in reader[1:]:
            for i, cat in enumerate(categories):
                totals[cat] += float(row[i + 1])

    print("\nTotal Expenses:", totals)
    print("Average Monthly Spending:", {cat: total / (len(reader) - 1) for cat, total in totals.items()})
    return totals

def visualize_expenses():
    totals = analyze_expenses()
    plt.bar(totals.keys(), totals.values(), color="skyblue")
    plt.xlabel("Categories"), plt.ylabel("Total Expenses ($)"), plt.title("Expenses Overview")
    plt.show()

# Menu
while (choice := input("\n1.Save 2.Analyze 3.Visualize 4.Exit: ")) != "4":
    {"1": save_expenses, "2": analyze_expenses, "3": visualize_expenses}.get(choice, lambda: print("Invalid"))()
