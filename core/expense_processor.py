import utilities.transaction_logger as transaction_logger
from core.input.date_input import txn_DateRecorder
from core.input.metadata_input import txn_MetadataRecorder
from core.input.amount_input import txn_AmtRecorder
import ui.section_banner


def expense_recorder():

    expense_transactions = {}

    ui.section_banner.heading_banner("EXPENSE")

    ## Expense recording section

    expense_amount = txn_AmtRecorder()

    ## Expense Source Section
    print(
        "\nWhere did you spend this money??\n[1] Housing & Rent \n[2] Loans & EMIs \n[3] Investments \n[4] Food & Groceries \n[5] Transportation \n[6] Bill & Utilities \n[7] Health Care \n[8] Shopping \n[9] Education & Learning \n[10] Travel & Hotel Bookings \n[11] Entertainment \n [12] Miscellaneous"
    )
    category = input("Please specify your income source: \t")
    while category not in [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
    ]:
        category = input("\033[31mInvalid input. Try again:\033[0m\t")

    match category:
        case "1":
            expense_category = "Housing & Rent"
        case "2":
            expense_category = "Loans & EMIs"
        case "3":
            expense_category = "Investments"
        case "4":
            expense_category = "Food & Groceries"
        case "5":
            expense_category = "Transportation"
        case "6":
            expense_category = "Bills & Utilities"
        case "7":
            expense_category = "Health Care"
        case "8":
            expense_category = "Shopping"
        case "9":
            expense_category = "Education & Learning"
        case "10":
            expense_category = "Travel & Hotel Bookings"
        case "11":
            expense_category = "Entertainment"
        case _:
            expense_category = (
                input("Please specify category:\t") or "Miscellaneous"
            )  # ? or <value> allows us to define a default value with input statement in case user submits blank value.

    ## Transaction Date
    transaction_date = txn_DateRecorder()

    ## Transaction metadata section
    transaction_metadata = txn_MetadataRecorder()

    ## updating transaction data into expense_transactions
    expense_transactions["transaction_date"] = transaction_date
    expense_transactions["transaction_category"] = expense_category
    expense_transactions["transaction_type"] = "DEBIT"
    expense_transactions["transaction_amount"] = expense_amount
    expense_transactions.update(transaction_metadata)

    ## Saving Transaction to Json
    transaction_logger.saveTransaction(expense_transactions, "EXPENSE")
