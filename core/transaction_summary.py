import json
import csv
from tabulate import tabulate


# todo 1: convert export to CSV to a module
# todo 2: fix CREDIT DEBIT data in CSV with ASCII Escape Sequennce codes coming in it
# todo 4: Add graphs for transactions for showing flow
def show_transaction_statement():
    # ? for variables, first transaction_logs_data for complete table &  transaction_table_row for individual row
    transaction_logs_data = []
    transaction_table_row = []

    # ? Loading json as a dictionary
    with open("./data/transactions.json") as file:
        transactions = json.load(file)

    # ? for extracting transaction data from nested dictionaries and appending it to table row: ps this caused bug the list not getting appened in as nested dictionaries but rather individual values in transaction_logs_data
    for txn in transactions.values():
        for txn_values in txn.values():
            if txn_values == "CREDIT":
                transaction_table_row.append("\033[32mCREDIT\033[0m")
            elif txn_values == "DEBIT":
                transaction_table_row.append("\033[31mDEBIT\033[0m")
            else:
                transaction_table_row.append(txn_values)
        transaction_logs_data.append(transaction_table_row)
        transaction_table_row = []

    # ? Sorting 2D List (transaction_logs_data, which contains all data of trasnaction to be displayed) based on date which is at index[0] hence the output comes based on chronological order
    transaction_logs_data.sort(key=lambda x: x[0])
    # ? for printing transaction summary in a tabular format like account statement
    if len(transaction_logs_data) < 1:
        print("\033[31mIt looks like you haven't made any transactions so far.\033[0m")
    else:
        section_heading = "\033[1;32m---------------------FinCLI Transaction Summary---------------------\033[0m"
        print(section_heading)
        print(
            tabulate(
                transaction_logs_data,
                headers=[
                    "\033[33mDate\033[0m",
                    "\033[33mCategory\033[0m",
                    "\033[33mType\033[0m",
                    "\033[33mAmount\033[0m",
                    "\033[33mMode\033[0m",
                    "\033[33mAccount\033[0m",
                    "\033[33mNote\033[0m",
                ],
                tablefmt="simple_grid",
            )
        )

    ## Export to csv functionality

    csv_decision = input(
        "\v\033[1;33mExport transaction statement to CSV? [y/n]:\033[0m "
    ).lower()

    while csv_decision not in ["y", "yes", "n", "no"]:
        csv_decision = input(
            "\033[31mInvalid input. Please enter 'y' or 'n':\033[0m "
        ).lower()

    if csv_decision in ["y", "yes"]:
        header_data = [
            "Trasnaction_Date",
            "Trasnaction_Category",
            "Trasnaction_Type",
            "Trasnaction_Amount",
            "Trasnaction_Mode",
            "Bank_Account",
            "Trasnaction_Note",
        ]
        with open(f"exports/Fincli_transaction_data.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header_data)
            writer.writerows(transaction_logs_data)
        print("\n\033[32mTransaction successfully exported!\033[0m\n")
