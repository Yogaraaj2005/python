#You are a college student trying to improve your budgeting by tracking your monthly expenses. You record spending in categories such as food, rent, utilities, and entertainment. You need a module that can: 

import csv
import matplotlib.pyplot as plt

FILENAME = "monthly_expenses.csv"

def save_expenses():
    num_categories = int(input("Enter the number of categories: "))
    num_months = int(input("Enter the number of months: "))

    categories = [input(f"Enter category {i+1} name: ") for i in range(num_categories)]

    # Creating the CSV file inside the function
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Month"] + categories)

        for month in range(1, num_months + 1):
            expenses = [input(f"Enter {category} expense for Month {month}: ") for category in categories]
            writer.writerow([f"Month {month}"] + expenses)

    print(f"Expenses saved to {FILENAME}.")

def analyze_expenses():
    with open(FILENAME, "r") as file:
        reader = list(csv.reader(file))
        categories = reader[0][1:]
        totals = {cat: 0 for cat in categories}

        for row in reader[1:]:
            for i, cat in enumerate(categories):
                totals[cat] += float(row[i + 1])

    print("\nTotal Expenses:")
    for cat, total in totals.items():
        print(f"{cat}: ${total:.2f}")

    print("\nAverage Monthly Expenses:")
    for cat, total in totals.items():
        print(f"{cat}: ${total / (len(reader) - 1):.2f}")

    return totals

def visualize_expenses():
    totals = analyze_expenses()
    plt.bar(totals.keys(), totals.values(), color="skyblue")
    plt.xlabel("Categories"), plt.ylabel("Total Expenses ($)"), plt.title("Total Expenses per Category")
    plt.show()

# Menu
while (choice := input("\n1. Save Expenses  2. Analyze Expenses  3. Visualize Expenses  4. Exit\nChoose an option: ")) != "4":
    {"1": save_expenses, "2": analyze_expenses, "3": visualize_expenses}.get(choice, lambda: print("Invalid option"))()
