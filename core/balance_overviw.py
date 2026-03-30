import json

# todo_1:  ADD networth of each account


def financial_overview_generator():
    net_income = 0.00
    net_expenses = 0.00
    net_worth = 0.00
    with open("./data/transactions.json") as file:
        transactions = json.load(file)

    if len(transactions) <= 0:
        print("Looks like you haven't made any transactions")
    else:

        for keys in transactions.values():
            if keys["transaction_type"] == "CREDIT":
                net_income += keys["transaction_amount"]
            elif keys["transaction_type"] == "DEBIT":
                net_expenses += keys["transaction_amount"]
        net_worth = round(net_income - net_expenses, 2)
        print(f"Your current networth is {net_worth}")
