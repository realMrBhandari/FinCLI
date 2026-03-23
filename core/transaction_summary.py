import json
from tabulate import tabulate


# todo 1: Add export to CSV Option in this transaction summary
# todo 2: Add graphs for transactions for showing flow
def show_transaction_statement():
    # ? for variables, first transaction_summary_table for complete table &  transaction_table_row for individual row
    transaction_summary_table = []
    transaction_table_row = []

    # ? Loading json as a dictionary
    with open("./data/transactions.json") as file:
        transactions = json.load(file)

    # ? for extracting transaction data from nested dictionaries and appending it to table row: ps this caused bug the list not getting appened in as nested dictionaries but rather individual values in transaction_summary_table
    for txn in transactions.values():
        for txn_values in txn.values():
            transaction_table_row.append(txn_values)
        transaction_summary_table.append(transaction_table_row)
        transaction_table_row = []

    # ? for printing transaction summary in a tabular format like account statement
    section_heading = "\033[1;32m---------------------FinCLI Transaction Summary---------------------\033[0m"
    print(section_heading)
    print(
        tabulate(
            transaction_summary_table,
            headers=[
                "\033[33mDate\033[0m",
                "\033[33mCategory\033[0m",
                "\033[33mType\033[0m",
                "\033[33mAmount\033[0m",
                "\033[33mAccount\033[0m",
                "\033[33mNote\033[0m",
            ],
            tablefmt="simple_grid",
        )
    )
