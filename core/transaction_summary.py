import json
from tabulate import tabulate


# todo 1: sorting transaction based on the recorded date
# todo 2: Add export to CSV Option in this transaction summary
# todo 3: Add graphs for transactions for showing flow
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
            if txn_values == "CREDIT":
                transaction_table_row.append("\033[32mCREDIT\033[0m")
            elif txn_values == "DEBIT":
                transaction_table_row.append("\033[31mDEBIT\033[0m")
            else:
                transaction_table_row.append(txn_values)
        transaction_summary_table.append(transaction_table_row)
        transaction_table_row = []

    # ? Sorting 2D List (transaction_summary_table, which contains all data of trasnaction to be displayed) based on date which is at index[0] hence the output comes based on chronological order
    transaction_summary_table.sort(key=lambda x: x[0])
    # ? for printing transaction summary in a tabular format like account statement
    if len(transaction_summary_table) < 1:
        print("\033[31mIt looks like you haven't made any transactions so far.\033[0m")
    else:
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
