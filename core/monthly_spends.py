import json

# import csv
from tabulate import tabulate
from datetime import datetime, timedelta


def montly_spends():

    # ? Loading json as a dictionary
    with open("./data/transactions.json") as file:
        transactions = json.load(file)

    print(
        """\033[1;32m===== Monthly Spend Summary =====\033[0m
    1. Current Month
    2. Previous Month
    3. Custom Range"""
    )

    user_choice = input("Choose an Option: ")
    while user_choice not in ["1", "2", "3"]:
        user_choice = input("Invalid Choice! Choose an approproate option from menu: ")

    if user_choice == "1":
        current_month = datetime.now().strftime("%Y_%m")
    elif user_choice == "2":
        previous_month = (datetime.now().replace(day=1) - timedelta(days=1)).strftime(
            "%Y_%m"
        )
    # ! Have to build a custom range month
    # elif user_choice == "3":
    #     custom_month_range = input("Please input ")

    def month_fetcher(arg):
        for outer_key in transactions:
            for inner_key in transactions[outer_key]:
                print(transactions[outer_key][inner_key])
