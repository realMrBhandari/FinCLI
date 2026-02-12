# ! Input Amount Code
# print("=== Your Income Records ===")
def income_recorder():
    print(
        """\033[1;32m===========================================================================
                             YOUR INCOME RECORDS
===========================================================================\033[0m\v"""
    )
    # ? Income recording section
    # !================     REFACTORING REGION  ================================================
    print("*income amount should be positive and numeric")
    input_income = input("Please input your income amount : \t")
    # todo: Implement trype conversion to float here and make sure the it is in two decimal points i.e in indian decimal system for recording monitoary value, also implement exception handling here so in case user passes some non numeric input here then the program should not crash while input get's converted into float and rather ask user again for valid numeric input and once float conversion is successfull the programme should moveon. So far this is the biggest obstacle for me in this code, I will proccede with integer input as of now and later convert it to floating type

    while not input_income.isdigit():
        print("\033[31mAttention User! Your input was invalid.\033[0m")
        income_amount = input("Only positive and numeric input allowed. Try again: \t")

    income_amount = int(input_income)
    # !================     REFACTORING REGION  ================================================

    # ? Income Source Section
    income_source = None
    print(
        "\n=== Please Enter Your Income Source ===\n1. Business \n2. Freelancing\n3. Salary \n4. Pocket Money \n5. Others "
    )
    category = input("Please specify your income source: \t")
    valid_inputs = ["1", "2", "3", "4", "5"]
    while category not in valid_inputs:
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
    print(
        f"\vYou earned \033[33m{income_amount} \033[0mfrom \033[33m{income_source}\033[0m, use it wisely."
    )


# ! All this can be wrapped in a function and and can be called over and over again from the FinCLI menu itself
