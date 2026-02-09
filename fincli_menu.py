import income_records

print(
    """\033[1;32m===========================================================================
                             FinCLI Finance Mneu
===========================================================================\033[0m\n 1. Income Records\n 2. Expense Records\n 3. View all transactions \n 4. Monthly Spends Summary \n 5. Exit \n"""
)

navigate = input("Pick a choice")

if navigate == "1":
    income_records.income_recorder()
