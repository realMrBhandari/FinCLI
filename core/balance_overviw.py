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
        print(f"Your current networth is {net_balance}")
