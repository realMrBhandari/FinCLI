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
    while (not module_floatChk.isItFloat(input_income)) or float(input_income) <= 1:
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
    # # Transaction metadata section
    # ? Transaction date
    print(
        """=== Date of Transaction ===
          1. Today 
          2. Custom Date"""
    )
    transaction_date_metadata = input("Please provide an option: ")
    while transaction_date_metadata not in ["1", "2"]:
        print("Invalid Input! Please Try Again!")
        transaction_date_metadata = input("Please provide an option b/w 1 & 2: ")
    if transaction_date_metadata == "1":
        transaction_date = datetime.now().date()
    # todo: Implement a function to turn this date into DD_MM_YYYY
    # ! Implement logic of custom date with validation and final formatting for DD-MM-YYYY
    else:
        # ? Transaction Year
        transaction_date_year = input("Please provide year of transaction: ")
        while (
            not transaction_date_year.isnumeric() or not len(transaction_date_year) == 4
        ) or (
            not int(transaction_date_year) == datetime.now().date().year
            and not int(transaction_date_year) < datetime.now().date().year
        ):
            print("Invalid Input! Please Try Again!")
            transaction_date_year = input("Please provide year of transaction: ")
        transaction_date = f"XX_XX_{transaction_date_year}"

    # ? transaction location
    transaction_location = (
        input("\nEnter the account in which the income was credited:\t") or "bank"
    )
    # ? transaction location
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

    # todo : implement transaction location feture as well, to differentiate where money was deposited to and where it was withdrawn from: transactionLocation, and implement a networth like feature showing where all money resides and for montly spends and transaction summary also add columns to show remaining balanaces in all accounts.

    # todo: implement date of transaction recodring as well, with a default and custom date feature.

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
