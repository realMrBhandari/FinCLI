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

    for outer_keys in transactions:
        for inner_keys in transactions[outer_keys]:
            if transactions[outer_keys][inner_keys] == "CREDIT":
                # todo: develop dict comparing logic
                key = transactions.get(outer_keys)
                print(key, bank_account_balance.get(key), "CREDIT")
            elif transactions[outer_keys][inner_keys] == "DEBIT":
                key = transactions.get(outer_keys)
                print(key, bank_account_balance.get(key), "DEBIT")

    for x in bank_account_balance:
        print(x, bank_account_balance[x])
