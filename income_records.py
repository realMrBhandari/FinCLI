import module_floatChk
from datetime import datetime


def income_recorder():
    #  Global Variable Zone
    income_transactions = (
        {}
    )  # ? dicitonary as a middlemen between userinputs and database
    print(
        """\033[1;32m===========================================================================
                             YOUR INCOME RECORDS
===========================================================================\033[0m\v"""
    )
    # def income_inputs():
    # # Income recording section
    # !================     REFACTORING REGION  ================================================
    print("*input should be positive and numeric")
    input_income = input("Please input your income amount:\t")

    # ? Short circuit is preventing programme from crashing here.
    while (not module_floatChk.isItFloat(input_income)) or float(input_income) <= 0:
        print("\033[31mAttention User! Your input was invalid.\033[0m")
        input_income = input("Only positive and numeric input allowed. Try again: \t")

    income_amount = round(float(input_income), 2)
    # !================     REFACTORING REGION  ===========================================
    # # Income Source Section
    print(
        "\n=== Please Enter Your Income Source ===\n1. Business \n2. Freelancing\n3. Salary \n4. Pocket Money \n5. Others "
    )
    category = input("Please specify your income source: \t")
    while category not in ["1", "2", "3", "4", "5"]:
        category = input("\033[31mInvalid input. Try again:\033[0m\t")
    match category:
        case "1":
            income_source = "Business"
        case "2":
            income_source = "Freelancing"
        case "3":
            income_source = "Salary"
        case "4":
            income_source = "Pocket Money"
        case "5":
            income_source = (
                input("Please specify your source:\t") or "Other sources"
            )  # ? or <value> allows us to define a default value with input statement in case user submits blank value.

    # # Transaction Date
    print(
        """\n=== Date of Transaction ===
        1. Today 
        2. Custom Date"""
    )
    transaction_date_menu = input("Please provide an option: ").strip(" ")
    while transaction_date_menu not in ["1", "2"]:
        print("\033[31mAttention User! Invalid Input, try again!\033[0m")
        transaction_date_menu = input("Please provide an option b/w 1 & 2: ")
    if transaction_date_menu == "1":
        transaction_date = datetime.now().date()
    # todo: Implement a function to turn this date into DD_MM_YYYY
    else:
        # ? Transaction Year -> year, ya to current year ke equal ho ya fir current year se lesser ho, agar input year current se jayda hai to loop karo taki correct year mil sake
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

        # ? Transaction Month; 2026 curent date -> month current month ke equal ho ya fir current month se lesser | if year < 2026 -> allow 1 - 12

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
        # ? Transaction Date: 31 range in [1,3,5,7,8,10,12]; 30 days in [4,6,9,11]; 2 - 28/29 based on leap year.
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
        transaction_date = f"{transaction_date_day.zfill(2)}_{transaction_date_month.zfill(2)}_{transaction_date_year}"

    # # Transaction metadata section
    # ? transaction location
    transaction_location = (
        input(
            "\nEnter the account in which the income was credited(20 characters max):\t"
        )
        or "bank"
    )
    while not len(transaction_location) <= 20:
        print(
            "\033[31mInvalid Input! Note should be between 1 to 50 characters long, try again!\033[0m"
        )
        transaction_location = (
            input(
                "\nEnter the account in which the income was credited(20 characters max):\t"
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

    income_transactions["income_amount"] = income_amount
    income_transactions["income_source"] = income_source
    income_transactions["transaction_date"] = transaction_date
    income_transactions["transaction_location"] = transaction_location
    income_transactions["transaction_note"] = transaction_note

    # ! To implement Recording these information to a database for transaction record and keeping track of balance

    # ! Implement Final Table in which records will be displayed to user
    print(
        f"\vRecorded income amount of \033[33m{income_transactions['income_amount']} \033[0mon \033[33m{income_transactions['transaction_date']} \033[0mfrom \033[33m{income_transactions['income_source']}\033[0m credited in \033[33m{income_transactions['transaction_location']}\033[0m account, was done for \033[33m{income_transactions['transaction_note']}\033[0m."
    )


# ! Decision State between user input and DB
# def input_Write():
#     print("Do You wish to finalise transaction ?")
#     user_decision = input(
#         "Type CONFIRM to finalise, else type REVERT to go back: "
#     ).lower()
#     while user_decision not in ["confirm", "revert"]:
#         print("Invalid Input! Try Again !")
#         user_decision = input(
#             "Type CONFIRM to finalise, else type REVERT to go back: "
#         ).lower()
#     if user_decision == "revert":
#         income_inputs()
#     else:
#          add the values stright into json
