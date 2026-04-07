import json

# todo_1:  ADD networth of each account


def financial_overview_generator():
    total_income = 0.00
    total_expenses = 0.00
    net_balance = 0.00
    with open("./data/transactions.json") as file:
        transactions = json.load(file)

    if len(transactions) <= 0:
        print("Looks like you haven't made any transactions")
    else:

        for keys in transactions.values():
            if keys["transaction_type"] == "CREDIT":
                total_income += keys["transaction_amount"]
            elif keys["transaction_type"] == "DEBIT":
                total_expenses += keys["transaction_amount"]
        net_balance = round(total_income - total_expenses, 2)

        print(f"Your running balance is {net_balance}")

    ## Balance in Individual Bank Accounts:
    unique_bank_accounts = set()
    for outer_key in transactions:
        for inner_key in transactions[outer_key]:
            if inner_key == "transaction_location":
                unique_bank_accounts.add(transactions[outer_key][inner_key])

    bank_account_balance = {}

    for x in unique_bank_accounts:
        bank_account_balance[x] = 0.00

    for lv1_key in transactions:
        bank_name = transactions[lv1_key]["transaction_location"]
        bank_txn_amount = transactions[lv1_key]["transaction_amount"]
        bank_txn_type = transactions[lv1_key]["transaction_type"]
        if bank_txn_type == "CREDIT":
            if bank_name in bank_account_balance:
                bank_account_balance[bank_name] += bank_txn_amount
        elif bank_txn_type == "DEBIT":
            if bank_name in bank_account_balance:
                bank_account_balance[bank_name] -= bank_txn_amount

    print(bank_account_balance)
