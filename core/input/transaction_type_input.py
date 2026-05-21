def get_txn_type():
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
