# ! Input Amount Code
# print("=== Your Income Records ===")
def income_recorder():
    print(
        """\033[1;32m===========================================================================
                             YOUR INCOME RECORDS
===========================================================================\033[0m\v"""
    )
    print("*income amount should be positive and numeric")
    income_amount = input("Please input your income amount : \t")
    while not income_amount.isdigit():
        print("\033[31mAttention User! Your input was invalid.\033[0m")
        income_amount = input("Only positive and numeric input allowed. Try again: \t")
    # todo: A type conversion is needed here, the user input which is string is needed to be converted into a numeric type once input for income amount is validated and implement expection handeling.

    # todo: Implement validation for negative & 0 inputs as well

    # todo: implement the industrial level of recording money, i guess money is not recorded in floating points, but whatever system it is money will be stored in that method.

    # ! Income Source Section
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
            )  # or <value> allows us to define a default value with input statement in case user submits blank value.
        # TODO ONE MORE CONDITION SHOULD BE IMPLEMENTED HERE WHERE THERE SHOULD BE A DEFAULT CASE IN CASE USER DOES NOT PROVIDE ANY INCOME SOURCE

    print(
        f"\vYou earned \033[33m{income_amount} \033[0mfrom \033[33m{income_source}\033[0m, use it wisely."
    )


# ! All this can be wrapped in a function and and can be called over and over again from the FinCLI menu itself
