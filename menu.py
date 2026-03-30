import core.income_processor as income_processor
import core.transaction_summary as transaction_summary
import core.balance_overviw as balance_overviw
import sys

print(
    """\033[1;32m===========================================================================
                             FinCLI Finance Menu
===========================================================================\033[0m\n 1. Record Income Transaction\n 2. Record Expense Transaction\n 3. View Transactions \n 4. Balance Overview \n 5. Monthly Sepnding Summary \n 6. Exit \n"""
)
navigate = input("Pick a choice:\t")

while navigate not in ["1", "2", "3", "4", "5"]:
    navigate = input("Your choice was invalid! Try Again:\t")
if navigate == "1":
    income_processor.income_recorder()
elif navigate == "2":
    print("\vFunctionality Under Development.")
elif navigate == "3":
    transaction_summary.show_transaction_statement()
elif navigate == "4":
    balance_overviw.financial_overview_generator()
elif navigate == "5":
    print("\vFunctionality Under Development.")
    sys.exit()
elif navigate == "5":
    print("Exiting the programme.....")
    sys.exit()
