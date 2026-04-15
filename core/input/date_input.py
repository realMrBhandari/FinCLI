from datetime import datetime, date

# todo --------------------------------------------------------------------------
# todo: [1] Refactor code using DRY
# todo: [2] Reduce compute
# todo: [3] Follow a clear variable name pattern
# todo --------------------------------------------------------------------------


red = "\033[31m"
reset = "\033[0m"


def transaction_date_logger():
    print(
        """\nWhen did this transaction occur?
 [1] Today 
 [2] Earlier this month
 [3] A specific date\n"""
    )

    #  Processing and validating user's choice
    user_input = input("Please provide an option: ").strip(" ")
    while user_input not in ["1", "2", "3"]:
        print(f"\033[31mAttention User! Invalid Input, try again!")
        user_input = input("Please provide an option b/w 1 & 2: ")

    #  Making decision on user's choice for determining date for trnaction
    if user_input == "1":  # gives us today's date
        transaction_date = datetime.now().date().strftime("%Y_%m_%d")

    elif user_input == "2":
        current_day = date.today().day
        earlier_date = input("Please provide tranasction date: ")
        while not earlier_date.isnumeric() or int(earlier_date) > current_day:
            if not earlier_date.isnumeric():
                print(f"{red}Invalid Input! {earlier_date} is not a number!{reset}")
            else:
                print(f"{red}Provided date {earlier_date} excceds current date{reset}")
            earlier_date = input("Please provide tranasction date: ")
        transaction_date = f"{datetime.now().strftime("%Y_%m")}_{earlier_date.zfill(2)}"

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
        transaction_date = f"{transaction_date_year}_{transaction_date_month.zfill(2)}_{transaction_date_day.zfill(2)}"
    return transaction_date
