# ? transaction bank_Account
def transaction_metadata_recorder():
    metadata = {}
    # ? transaction mode
    transaction_mode = (
        input("\nEnter transaction mode (e.g., Cash, Card, UPI) [max 20 chars]: \t")
        or "-"
    )
    while not len(transaction_mode) <= 20:
        transaction_mode = (
            input(
                "\n\033[31mInvalid input. Enter transaction mode (1–20 characters, e.g., Cash, Card, UPI):\033[0m "
            )
            or "—"
        )
    # ? account
    transaction_bank_account = (
        input(
            "\nEnter the account in which the income was credited(20 characters max):\t"
        )
        or "bank"
    )
    while not len(transaction_bank_account) <= 20:
        print()
        transaction_bank_account = (
            input(
                "\n\033[31mAccount name must be 1–20 characters. Enter the account where income was credited:\033[0m "
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

    metadata["transaction_mode"] = transaction_mode
    metadata["transaction_bank_account"] = transaction_bank_account
    metadata["transaction_note"] = transaction_note
    return metadata
