import core.income_processor as income_processor
import sys

print(
    """\033[1;32m===========================================================================
                             FinCLI Finance Menu
===========================================================================\033[0m\n 1. Income Records\n 2. Expense Records\n 3. View all transactions \n 4. Networth and All Account Summary \n 5. Monthly Sepnding Summary \n 6. Exit \n"""
)
navigate = input("Pick a choice:\t")

while navigate not in ["1", "2", "3", "4", "5"]:
    navigate = input("Your choice was invalid! Try Again:\t")
if navigate == "1":
    income_processor.income_recorder()
elif navigate == "2":
    print("\vFunctionality Under Development.")
elif navigate == "3":
    print("\vFunctionality Under Development.")
elif navigate == "4":
    print("\vFunctionality Under Development.")
elif navigate == "5":
    print("\vFunctionality Under Development.")
    sys.exit()
elif navigate == "5":
    print("Exiting the programme.....")
    sys.exit()
