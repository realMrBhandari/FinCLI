from utilities.amount_validator import isItFloat

red = "\033[31m"
rest = "\033[0m"


def txn_AmtRecorder():

    input_amt = input("Please input transaction amount:\t")

    # ? Short circuit is preventing programme from crashing here.
    while (not isItFloat(input_amt)) or float(input_amt) <= 0:

        if not isItFloat(input_amt):
            print(f"{red}Your input {input_amt} is not a number{rest}.")
        elif float(input_amt) <= 0:
            print(f"{red}Your input {input_amt} is equal to 0{rest}.")

        input_amt = input("Please input transaction income amount: \t")

    amt_normalized = round(float(input_amt), 2)
    return amt_normalized
