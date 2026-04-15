import core.income_processor as income_processor
import core.expense_processor
import core.transaction_summary as transaction_summary
import core.balance_overviw as balance_overviw
import core.monthly_spends as monthly_spends
import sys
import ui.ui_menu as ui_menu

menu = """\033[1;33m===========================================================================
                              FinCLI Finance Menu
===========================================================================\n [1] Record Income Transaction\n [2] Record Expense Transaction\n [3] View Transactions \n [4] Balance Overview \n [5] Monthly Sepnding Summary \n [6] Exit \n===========================================================================\033[0m \n"""


# ! action dispatcher, for triggering appropriate functionality based on user's choice
def trigger_action(trigger):
    if trigger == "1":
        income_processor.income_recorder()
    elif trigger == "2":
        core.expense_processor.expense_recorder()
    elif trigger == "3":
        transaction_summary.show_transaction_statement()
    elif trigger == "4":
        balance_overviw.financial_overview_generator()
    elif trigger == "5":
        monthly_spends.montly_spends()
    elif trigger == "6":
        print("Exiting the programme.....")
        sys.exit()


# ! REPL loop for keeping programme persitant and maintain it's state


def repl():
    while True:
        # ? Printing FinCLI menu
        # ui_menu.rich_fincli_menu()  ? will add later when UI will be implemented right now nelow code will be used
        print(menu)

        # ? REPL Core Logic
        navigate = input("Pick a choice (1 - 6):\t")
        while navigate not in ["1", "2", "3", "4", "5", "6"]:
            navigate = input(
                f"\033[31;1mYour choice {navigate} was invalid! Try Again: \033[0m"
            )

        trigger_action(navigate)


# ! calling REPL loop to begin programme

repl()
