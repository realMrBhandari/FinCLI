import utilities.transaction_logger as transaction_logger
from core.input.date_input import txn_DateRecorder
from core.input.metadata_input import txn_MetadataRecorder
from core.input.amount_input import txn_AmtRecorder
import ui.section_banner


def income_recorder():

    income_transactions = {}
    ui.section_banner.heading_banner("INCOME")

    ## Income recording section
    income_amount = txn_AmtRecorder()

    ## Income Source Section
    print(
        "\nSelect income source:\n[1] Business \n[2] Freelancing\n[3] Salary \n[4] Pocket Money \n[5] Other"
    )
    category = input("Selection:\t")
    while category not in ["1", "2", "3", "4", "5"]:
        category = input(
            "\033[31mInvalid selection. Please enter a valid option:\033[0m\t"
        )
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
            income_source = input("Enter income source:\t") or "Other sources"

    ## Transaction Date
    transaction_date = txn_DateRecorder()

    ## Transaction metadata section
    transaction_metadata = txn_MetadataRecorder()

    ## updating transaction data into income_transactions
    income_transactions["transaction_date"] = transaction_date
    income_transactions["transaction_category"] = income_source
    income_transactions["transaction_type"] = "CREDIT"
    income_transactions["transaction_amount"] = income_amount
    income_transactions.update(transaction_metadata)

    ## Saving Transaction to Json
    transaction_logger.saveTransaction(income_transactions, "INCOME")
