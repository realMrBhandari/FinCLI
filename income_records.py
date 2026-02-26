import module_floatChk


def income_recorder():
    print(
        """\033[1;32m===========================================================================
                             YOUR INCOME RECORDS
===========================================================================\033[0m\v"""
    )
    # ? Income recording section
    # !================     REFACTORING REGION  ================================================
    print("*input should be positive and numeric")
    input_income = input("Please input your income amount : \t")

    while not module_floatChk.isItFloat(input_income):
        print("\033[31mAttention User! Your input was invalid.\033[0m")
        input_income = input("Only positive and numeric input allowed. Try again: \t")

    income_amount = float(input_income)
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
    # ! To implement Recording these information to a database for transaction record and keeping track of balance
    print(
        f"\vRecorded income amount of \033[33m{income_amount} \033[0mfrom \033[33m{income_source}\033[0m."
    )
