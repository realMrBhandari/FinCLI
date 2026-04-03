import json
import copy
import csv
from tabulate import tabulate


# todo 1: convert export to CSV to a module
# todo 4: Add graphs for transactions for showing flow
def show_transaction_statement():
    ## Extracting values from the JSON and storing it as a 2D List (becasue tabulate uses 2d List for creating table rows)

    # ? for variables, first transactions_data for complete table &  transaction_row for individual row
    transactions_data = []  # for row in tabulate
    transaction_row = []  # container for converted row from dictionary transaction

    # ? Loading json as a dictionary
    with open("./data/transactions.json") as file:
        transactions = json.load(file)

    # ? for extracting transaction data from nested dictionaries and appending it to table row: ps this caused bug the list not getting appened in as nested dictionaries but rather individual values in transactions_data

    for txn in transactions.values():
        for txn_values in txn.values():
            transaction_row.append(txn_values)
        transactions_data.append(transaction_row)
        transaction_row = []

    # ? Sorting 2D List (transactions_data, which contains all data of trasnaction to be displayed) based on date which is at index[0] hence the output comes based on chronological order
    transactions_data.sort(key=lambda x: x[0])

    ## Tabulate specific block: For using trasnactions data and printing it as a table using tabulat || adding color codes to debit and credit
    # ? UI element for ALL transaction SUmmary table:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    # ? creating a seprate list for tabulate and Altering values in rows for Credit and Debit
    tabulate_rows = copy.deepcopy(
        transactions_data
    )  # deep copy prevents mutating original structure here it might look like we are assigining values from transactions_data to tabulate_row but we are passing just the refrence
    for row in tabulate_rows:
        if row[2] == "DEBIT":
            row[2] = f"{RED}{row[2]}{RESET}"
            row[3] = f"{RED}{row[3]}{RESET}"
        elif row[2] == "CREDIT":
            row[2] = f"{GREEN}{row[2]}{RESET}"
            row[3] = f"{GREEN}{row[3]}{RESET}"

    # ? for printing transaction summary in a tabular format like account statement
    if len(transactions_data) < 1:
        print("\033[31mIt looks like you haven't made any transactions so far.\033[0m")
    else:
        section_heading = "\033[1;32m---------------------FinCLI Transaction Summary---------------------\033[0m"
        print(section_heading)
        print(
            tabulate(
                tabulate_rows,
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
            writer.writerows(transactions_data)
        print("\n\033[32mTransaction successfully exported!\033[0m\n")
