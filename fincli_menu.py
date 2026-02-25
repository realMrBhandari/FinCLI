import income_records
import sys

print(
    """\033[1;32m===========================================================================
                             FinCLI Finance Mneu
===========================================================================\033[0m\n 1. Income Records\n 2. Expense Records\n 3. View all transactions \n 4. Monthly Spends Summary \n 5. Exit \n"""
)
navigate = input("Pick a choice:\t")

while navigate not in ["1", "2", "3", "4", "5"]:
    navigate = input("Your choice was invalid! Try Again:\t")
if navigate == "1":
    income_records.income_recorder()
elif navigate == "2":
    print("\vFunctionality Under Development.")
elif navigate == "3":
    print("\vFunctionality Under Development.")
elif navigate == "4":
    print("\vFunctionality Under Development.")
elif navigate == "5":
    print("Exiting the programme.....")
    sys.exit()
