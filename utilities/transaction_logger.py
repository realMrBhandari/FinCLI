from datetime import datetime
import json
import os
from tabulate import tabulate


def saveTransaction(transaction, record):
    # ? Transaction ID for each unique transaction, so no two transacations can overlap:
    transaction_id = datetime.now().strftime("%Y_%m_%d_%H:%M:%S")

    # ? read json data for transactions
    if os.path.exists("data/transactions.json"):
        with open("data/transactions.json", "r") as json_file:
            stored_transactions = json.load(json_file)
    else:
        stored_transactions = {}  # Start with an empty dictionary if file doesn't exist

    stored_transactions[transaction_id] = transaction

    # ? write the json file with the transaction
    with open("data/transactions.json", "w") as json_file:
        json.dump(stored_transactions, json_file, indent=4)

    print("""\n\033[32mTransaction recorded successfully.\033[0m""")

    table = [
        [
            transaction["transaction_date"],
            transaction["transaction_category"],
            transaction["transaction_amount"],
            transaction["transaction_mode"],
            transaction["transaction_bank_account"],
            transaction["transaction_note"],
        ]
    ]

    if record == "INCOME":
        header = [
            "\033[33mTransaction Date\033[0m",
            "\033[33mIncome Source\033[0m",
            "\033[33mAmount Cr.\033[0m",
            "\033[33mMode.\033[0m",
            "\033[33mAccount\033[0m",
            "\033[33mNote\033[0m",
        ]
    elif record == "EXPENSE":
        header = [
            "\033[33mTransaction Date\033[0m",
            "\033[33mExpense Category\033[0m",
            "\033[33mAmount db..\033[0m",
            "\033[33mMode.\033[0m",
            "\033[33mAccount\033[0m",
            "\033[33mNote\033[0m",
        ]
    print(
        tabulate(
            table,
            headers=header,
            tablefmt="simple_outline",
        )
    )
