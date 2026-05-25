# ? core modules
from core.add_transactions import record_transaction
from core.transaction_history import display_transactions

# ? Database realted module
from database.setup_db import create_database

# ? 3rd party modules
from pathlib import Path
import sys

# ! following code will create database if it does not exist
file_path = Path("database/fincil.db")
if not file_path.is_file():
    create_database()

# # Menu starts from here
menu = """\033[1;33m===========================================================================
                              FinCLI Finance Menu
===========================================================================\n [1] Record Transactions\n [2] View Transactions \n [3] Balance Overview \n [4] Monthly Sepnding Summary \n [5] Exit \n===========================================================================\033[0m \n"""


# ! action dispatcher, for triggering appropriate functionality based on user's choice
def trigger_action(trigger):
    if trigger == "1":
        record_transaction()
    elif trigger == "2":
        display_transactions()
    elif trigger == "3":
        print("Under Development")
    elif trigger == "4":
        print("Under Development")
    elif trigger == "5" or "exit" or "EXIT":
        print("Exiting the programme.....")
        sys.exit()


# ! REPL loop for keeping programme persitant and maintain it's state


def repl():
    while True:
        # ? Printing FinCLI menu
        print(menu)

        # ? REPL Core Logics
        navigate = input("Pick a choice (1 - 5):\t")
        while navigate not in ["1", "2", "3", "4", "5", "exit", "EXIT"]:
            navigate = input(
                f"\033[31;1mYour choice {navigate} was invalid! Try Again: \033[0m"
            )

        trigger_action(navigate)


# ! calling REPL loop to begin programme

repl()
