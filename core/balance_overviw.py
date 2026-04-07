import json
from tabulate import tabulate

# todo_1:  modularize + refactor code
# todo 2: fix variable names with more meaningful and self descriptive name and eliminate all the vagueness || also applicable for, for loop where i see vague names for placeholder names


def financial_overview_generator():
    # ? normalizing each value with zero
    total_income = 0.00
    total_expenses = 0.00
    net_balance = 0.00

    # ? loading JSON data into a dictionary
    with open("./data/transactions.json") as file:
        transactions = json.load(file)

    # ? Calculating & displaying net balance
    if len(transactions) <= 0:
        print("Looks like you haven't made any transactions")
    else:
        for keys in transactions.values():
            if keys["transaction_type"] == "CREDIT":
                total_income += keys["transaction_amount"]
            elif keys["transaction_type"] == "DEBIT":
                total_expenses += keys["transaction_amount"]
        net_balance = round(total_income - total_expenses, 2)
        print(
            tabulate(
                [["\033[1;33mClosing Balance\033[0m", net_balance]],
                tablefmt="heavy_grid",
            )
        )

    ## Balance in Individual Bank Accounts:

    # ? using set for extracting bank account names from transctions data ensuing unique values
    unique_bank_accounts = set()
    for outer_key in transactions:
        for inner_key in transactions[outer_key]:
            if inner_key == "transaction_location":
                unique_bank_accounts.add(transactions[outer_key][inner_key])

    # ? creating a dynamic dictionary with each bank account as a key using set
    bank_account_balance = {}
    for x in unique_bank_accounts:
        bank_account_balance[x] = 0.00

    # ? For calculating balance for each account
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

    # ? For printing table containing all account balance
    account_balance_row = []
    for account_name in bank_account_balance:
        bank_account = []
        bank_account.append(account_name)
        bank_account.append(bank_account_balance.get(account_name))
        account_balance_row.append(bank_account)
        bank_account = []

    account_balance_row.sort()
    print(
        tabulate(
            account_balance_row,
            headers=["\033[1;33mBank Account", "Running Balance\033[0m"],
            tablefmt="simple_grid",
        )
    )
