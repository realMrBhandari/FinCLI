import core.transaction_summary as transaction_summary
import core.balance_overviw as balance_overviw
import core.monthly_spends as monthly_spends
import sys
from core.record_transaction import record_transactions

menu = """\033[1;33m===========================================================================
                              FinCLI Finance Menu
===========================================================================\n [1] Record Transactions\n [2] View Transactions \n [3] Balance Overview \n [4] Monthly Sepnding Summary \n [5] Exit \n===========================================================================\033[0m \n"""


# ! action dispatcher, for triggering appropriate functionality based on user's choice
def trigger_action(trigger):
    if trigger == "1":
        record_transactions()
    elif trigger == "2":
        transaction_summary.show_transaction_statement()
    elif trigger == "3":
        balance_overviw.financial_overview_generator()
    elif trigger == "4":
        monthly_spends.montly_spends()
    elif trigger == "5":
        print("Exiting the programme.....")
        sys.exit()


# ! REPL loop for keeping programme persitant and maintain it's state


def repl():
    while True:
        # ? Printing FinCLI menu
        # ui_menu.rich_fincli_menu()  ? will add later when UI will be implemented right now nelow code will be used
        print(menu)

        # ? REPL Core Logic
        navigate = input("Pick a choice (1 - 5):\t")
        while navigate not in ["1", "2", "3", "4", "5"]:
            navigate = input(
                f"\033[31;1mYour choice {navigate} was invalid! Try Again: \033[0m"
            )

        trigger_action(navigate)


# ! calling REPL loop to begin programme

repl()
