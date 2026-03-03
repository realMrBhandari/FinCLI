import module_floatChk


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
    # ? Income recording section
    # !================     REFACTORING REGION  ================================================
    print("*input should be positive and numeric")
    input_income = input("Please input your income amount:\t")

    # ? Short circuit is preventing programme from crashing here.
    while (not module_floatChk.isItFloat(input_income)) or float(input_income) <= 1:
        print("\033[31mAttention User! Your input was invalid.\033[0m")
        input_income = input("Only positive and numeric input allowed. Try again: \t")

    income_amount = round(float(input_income), 2)
    # !================     REFACTORING REGION  ===========================================
    # ? Income Source Section
    income_source = None
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
    transaction_location = (
        input("\nEnter the account in which the income was credited:\t") or "bank"
    )
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
    income_transactions["transaction_location"] = transaction_location
    income_transactions["transaction_note"] = transaction_note

    # todo : implement transaction location feture as well, to differentiate where money was deposited to and where it was withdrawn from: transactionLocation, and implement a networth like feature showing where all money resides and for montly spends and transaction summary also add columns to show remaining balanaces in all accounts.

    # todo: implement date of transaction recodring as well, with a default and custom date feature.

    # ! To implement Recording these information to a database for transaction record and keeping track of balance

    # ! Implement Final Table in which records will be displayed to user
    print(
        f"\vRecorded income amount of \033[33m{income_transactions['income_amount']} \033[0mfrom \033[33m{income_transactions['income_source']}\033[0m credited in \033[33m{income_transactions['transaction_location']}\033[0m account, was done for \033[33m{income_transactions['transaction_note']}\033[0m."
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
#         # add the values stright into json
