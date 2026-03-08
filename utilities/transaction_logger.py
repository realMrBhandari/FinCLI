from datetime import datetime
import json
import os


def saveTransaction(transaction):
    # ? Transaction ID for each unique transaction, so no two transacations can overlap:
    transaction_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

    print(
        f"\vRecorded income amount of \033[33m{transaction['income_amount']} \033[0mon \033[33m{transaction['transaction_date']} \033[0mfrom \033[33m{transaction['income_source']}\033[0m credited in \033[33m{transaction['transaction_location']}\033[0m account, was done for \033[33m{transaction['transaction_note']}\033[0m."
    )
