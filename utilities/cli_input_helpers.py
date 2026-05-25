from utilities.amount_validator import isItFloat
from datetime import datetime, date

red = "\033[31m"
green = "\033[32m"
reset = "\033[0m"


# //============================================================================================================================================================================================================


## this function deals with processing validating input amount
def amount_processor():

    input_amt = input("Please input transaction amount: ")

    # ? Short circuit is preventing programme from crashing here.
    while (not isItFloat(input_amt)) or float(input_amt) <= 0:

        if not isItFloat(input_amt):
            print(f"{red}Your input {input_amt} is not a number{reset}.")
        elif float(input_amt) <= 0:
            print(f"{red}Your input {input_amt} is equal to 0{reset}.")

        input_amt = input("Please input transaction income amount: ")

    amt_normalized = round(float(input_amt), 2)
    return amt_normalized


# //============================================================================================================================================================================================================


def transaction_side():
    txn_type = input(
        "Specify the type of transaction\n"
        "[1] Income transaction\n"
        "[2] Expense transaction\n"
        "Choose an appropriate option 1 - 2: "
    )

    while not txn_type.isdigit() or txn_type not in ["1", "2"]:
        print("\033[31mInvalid input. Try again!\033[0m")
        txn_type = input("Choose an appropriate option 1 - 2: ")

    # ! UI to be handled seprately in future updates
    (
        print(
            "\033[1;32m ========================== Income Transaction Recording ==========================\033[0m\n"
        )
        if txn_type == "1"
        else print(
            "\033[1;31m ========================== Expense Transaction Recording ==========================\033[0m\n"
        )
    )

    return txn_type


# //============================================================================================================================================================================================================


## this function deals with mapping amunt to category
def map_transaction_category(choice):
    # ! NOTE: choice is that value which decides what transaction it is, if choice == 1 then it is income transaction else it is expense transction since we have binary logic here either it is income or it is expense, but I believe invalidating user inputs so for expense the choice value will be 2, but anyways any value which is not 1 will be considered as expense which is not the case as my previous step will never allow it
    # ? category data is stored in dictionaries allowing us to remove or edit categories in future should I implement an oboarding screen
    category_income = {
        1: "Business",
        2: "Freelancing",
        3: "Monthy Salary",
        4: "Bonus",
        4: "Pocket Money",
        5: "Others",
    }

    category_expense = {
        1: "Housing & Rent",
        2: "Loans & EMIs",
        3: "Investments",
        4: "Food & Groceries",
        5: "Transportation",
        6: "Bill & Utilities",
        7: "Health Care",
        8: "Shopping",
        9: "Education & Learning",
        10: "Travel & Hotel Bookings",
        11: "Entertainment",
        12: "Miscellaneous",
    }

    # ? prompting user for category message based on argument using ternary operator
    print(
        "Please Select Your Income Source"
        if choice == 1
        else "Where Was This Money Spent?"
    )

    #  making use of ternary operator to decide which dictionary to pick and ampping it to the argument provided so we don't have to use multiple if else statements in the code just to decide which dictionary to pick, making code shorter and honour DRY Principle
    map_category = category_income if choice == 1 else category_expense

    #  using for loop to extract keys and values from rhe dicitonary and printing them serially like a menu of choices, making use of .items() on dictionary mapped to the choice dictionary method and unpacking tupleusinf key, value in for loop
    for key, value in map_category.items():
        print(f"[{key}] {value}")

    # ? Prompting user to pick a transaction category as well as validating user inputs
    category_selection = input(
        f"Input your choice of category 1- {len(map_category)}: "
    )
    while (
        not category_selection.isdigit() or int(category_selection) not in map_category
    ):
        print(f"{red}Invalid selection. Try again!{reset}")
        category_selection = input(
            f"Input your choice of category 1- {len(map_category)}: "
        )

    # ? the transction category will be retruned back to the caller
    return map_category[int(category_selection)]


# //============================================================================================================================================================================================================

## transaction date mapping module

# todo --------------------------------------------------------------------------
# todo: [1] Refactor code using DRY
# todo: [2] Reduce compute
# todo: [3] Follow a clear variable name pattern
# todo --------------------------------------------------------------------------


red = "\033[31m"
reset = "\033[0m"


def ask_transaction_date():
    print("""\nWhen did this transaction occur?
 [1] Today 
 [2] Earlier this month
 [3] A specific date\n""")

    #  Processing and validating user's choice
    user_input = input("Please provide an option: ").strip(" ")
    while user_input not in ["1", "2", "3"]:
        print(f"\033[31mAttention User! Invalid Input, try again! \033[0m")
        user_input = input("Please provide an option b/w 1 & 3: ")

    #  Making decision on user's choice for determining date for trnaction
    if user_input == "1":  # gives us today's date
        transaction_date = datetime.now().date().strftime("%Y-%m-%d")

    elif user_input == "2":
        current_day = date.today().day
        earlier_date = input("Please provide tranasction date: ")
        while not earlier_date.isnumeric() or int(earlier_date) > current_day:
            if not earlier_date.isnumeric():
                print(f"{red}Invalid Input! {earlier_date} is not a number!{reset}")
            else:
                print(f"{red}Provided date {earlier_date} excceds current date{reset}")
            earlier_date = input("Please provide tranasction date: ")
        transaction_date = f"{datetime.now().strftime("%Y-%m")}-{earlier_date.zfill(2)}"

    else:  # will let user's manually provide date
        # //  Transaction Year -> year, ya to current year ke equal ho ya fir current year se lesser ho, agar input year current se jayda hai to loop karo taki correct year mil sake
        print(
            f"\033[33m*Numeric: Can only record YEAR between 2000 and {datetime.now().date().year}\033[0m"
        )
        transaction_date_year = input("Transaction YEAR: ").strip(" ")
        while (
            (
                not transaction_date_year.isnumeric()
                or not len(transaction_date_year) == 4
            )
            or (
                not int(transaction_date_year) == datetime.now().date().year
                and not int(transaction_date_year) < datetime.now().date().year
            )
            or int(transaction_date_year) < 2000
        ):
            print("\033[31mAttention User! Invalid Input, try again!\033[0m")
            transaction_date_year = input(
                "Please provide a valid Transaction Year: "
            ).strip(" ")

        # // Transaction Month; 2026 curent date -> month current month ke equal ho ya fir current month se lesser | if year < 2026 -> allow 1 - 12

        if int(transaction_date_year) == datetime.now().date().year:
            print(
                f"\033[33m*Numeric: Can only record MONTH between 1 and current month({datetime.now().date().month})\033[0m"
            )
            transaction_date_month = input("Transaction MONTH: ").strip(" ")
            while (
                not transaction_date_month.isnumeric()
                or not int(transaction_date_month) <= datetime.now().date().month
            ):
                print("\033[31mAttention User! Invalid Input, try again!\033[0m")
                transaction_date_month = input(
                    "Please provide a valid Transaction Month: "
                ).strip(" ")
        elif int(transaction_date_year) < datetime.now().date().year:
            print(f"\033[33m*Numeric: Can only record MONTH between 1 and 12\033[0m")
            transaction_date_month = input(
                f"Transaction MONTH for year {transaction_date_year}: "
            ).strip(" ")
            while not transaction_date_month.isnumeric() or int(
                transaction_date_month
            ) not in range(1, 13):
                print("\033[31mAttention User! Invalid Input, try again!\033[0m")
                transaction_date_month = input(
                    "Please provide a valid Transaction Month: "
                ).strip(" ")
        # // Transaction Date: 31 range in [1,3,5,7,8,10,12]; 30 days in [4,6,9,11]; 2 - 28/29 based on leap year.
        if (
            int(transaction_date_year) == datetime.now().date().year
            and int(transaction_date_month) == datetime.now().date().month
        ):
            print(
                f"\033[33m*Numeric: Can only record DAY between 1 and {datetime.now().date().day}\033[0m"
            )
            transaction_date_day = input("Transaction DAY: ").strip(" ")
            while (
                not transaction_date_day.isnumeric()
                or not int(transaction_date_day) <= datetime.now().date().day
                or int(transaction_date_day) < 1
            ):
                print("\033[31mAttention User! Invalid Input, try again!\033[0m")
                transaction_date_day = input(
                    "Please provide a valid Transaction Day: "
                ).strip(" ")
        else:
            if transaction_date_month in ["1", "3", "5", "7", "8", "10", "12"]:
                print(f"\033[33m*Numeric: Can only record DAY between 1 and 31\033[0m")
                transaction_date_day = input(
                    f"Transaction DAY for month {datetime.now().date().month}: "
                ).strip(" ")
                while not transaction_date_day.isnumeric() or int(
                    transaction_date_day
                ) not in range(1, 32):
                    transaction_date_day = input(
                        "Please provide a valid Transaction Day: "
                    ).strip(" ")
            elif transaction_date_month in ["4", "6", "9", "11"]:
                print("\033[33m*Numeric: Can only record DAY between 1 and 30\033[0m")
                transaction_date_day = input(
                    f"Transaction DAY for month {datetime.now().date().month}: "
                ).strip(" ")
                while (
                    not transaction_date_day.isnumeric()
                    or transaction_date_day not in range(1, 31)
                ):
                    print("\033[31mAttention User! Invalid Input, try again!\033[0m")
                    transaction_date_day = input(
                        "Please provide a valid Transaction Day: "
                    ).strip(" ")
            elif transaction_date_month == "2":
                if (
                    int(transaction_date_year) % 4 == 0
                    and int(transaction_date_year) % 100 != 0
                ) or (int(transaction_date_year) % 400 == 0):
                    print(
                        f"\033[33m*Numeric: Can only record DAY between 1 and 29\033[0m"
                    )
                    transaction_date_day = input("Transaction DAY: ").strip(" ")
                    while not transaction_date_day.isnumeric() or int(
                        transaction_date_day
                    ) not in range(1, 30):
                        print(
                            "\033[31mAttention User! Invalid Input, try again!\033[0m"
                        )
                        transaction_date_day = input(
                            "Please provide a valid Transaction Day: "
                        ).strip(" ")
                else:
                    print(
                        f"\033[33m*Numeric: Can only record DAY between 1 and 28\033[0m"
                    )
                    transaction_date_day = input("Transaction DAY: ").strip(" ")
                    while not transaction_date_day.isnumeric() or int(
                        transaction_date_day
                    ) not in range(1, 29):
                        print(
                            "\033[31mAttention User! Invalid Input, try again!\033[0m"
                        )
                        transaction_date_day = input(
                            "Please provide a valid Transaction Day: "
                        ).strip(" ")
        transaction_date = f"{transaction_date_year}-{transaction_date_month.zfill(2)}-{transaction_date_day.zfill(2)}"
    return transaction_date


# //============================================================================================================================================================================================================
# ? transaction bank_Account
def get_transaction_metadata():
    metadata = {}
    # ? transaction mode
    transaction_mode = (
        input("\nEnter transaction mode (e.g., Cash, Card, UPI) [max 20 chars]: \t")
        or "-"
    )
    while not len(transaction_mode) <= 20:
        transaction_mode = (
            input(
                "\n\033[31mInvalid input. Enter transaction mode (1–20 characters, e.g., Cash, Card, UPI):\033[0m "
            )
            or "—"
        )
    # ? account
    transaction_bank_account = (
        input(
            "\nEnter the account in which the income was credited(20 characters max):\t"
        )
        or "bank"
    )
    while not len(transaction_bank_account) <= 20:
        print()
        transaction_bank_account = (
            input(
                "\n\033[31mAccount name must be 1–20 characters. Enter the account where income was credited:\033[0m "
            )
            or "bank"
        )
    # ? transaction note
    transaction_note = input(
        "\nAdd a note to describe your transaction (50 characters max): "
    )
    while len(transaction_note) > 50 or len(transaction_note) < 1:
        print(
            "\033[31mInvalid Input! Note should be between 1 to 50 characters long, try again!\033[0m"
        )
        transaction_note = input("Add a note to describe your transaction: ")

    return transaction_mode, transaction_bank_account, transaction_note


# //============================================================================================================================================================================================================
