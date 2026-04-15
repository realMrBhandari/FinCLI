import utilities.amount_validator as amount_validator
import utilities.transaction_logger as transaction_logger
import utilities.transaction_date_handler
import utilities.transaction_metadata_handler


def income_recorder():

    income_transactions = (
        {}
    )  # ? dicitonary as a middlemen between userinputs and database
    print(
        """\033[1;32m===========================================================================
                             YOUR INCOME RECORDS
===========================================================================\033[0m\v"""
    )

    ## Income recording section
    print("*input should be positive and numeric")
    input_income = input("Please input your income amount:\t")

    # ? Short circuit is preventing programme from crashing here.
    while (not amount_validator.isItFloat(input_income)) or float(input_income) <= 0:
        print("\033[31mAttention User! Your input was invalid.\033[0m")
        input_income = input("Only positive and numeric input allowed. Try again: \t")

    income_amount = round(float(input_income), 2)

    ## Income Source Section
    print(
        "\nWhat is the source of this income?\n[1] Business \n[2] Freelancing\n[3] Salary \n[4] Pocket Money \n[5] Others "
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

    ## Transaction Date
    transaction_date = utilities.transaction_date_handler.transaction_date_logger()

    ## Transaction metadata section
    transaction_metadata = (
        utilities.transaction_metadata_handler.transaction_metadata_recorder()
    )

    ## updating transaction data into income_transactions
    income_transactions["transaction_date"] = transaction_date
    income_transactions["transaction_category"] = income_source
    income_transactions["transaction_type"] = "CREDIT"
    income_transactions["transaction_amount"] = income_amount
    income_transactions.update(transaction_metadata)

    ## Saving Transaction to Json
    transaction_logger.saveTransaction(income_transactions)
