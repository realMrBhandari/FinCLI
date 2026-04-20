import utilities.transaction_logger as transaction_logger
import utilities.txn_categories as categories_of_transaction
from core.input.date_input import txn_DateRecorder
from core.input.metadata_input import txn_MetadataRecorder
from core.input.amount_input import txn_AmtRecorder
import ui.section_banner


def transaction_processor():
    transactions_params = {}

    # ! transaction side
    print(
        "What would you like to record? \n[1] Income transaction \n[2] Expense transaction"
    )
    txn_type_choice = input("Select an option 1 - 2: ")
    while txn_type_choice not in ["1", "2"]:
        print("\033[31mInvalid input. Try again:\033[0m\t")
        txn_type_choice = input("Select an option 1 - 2: ")

    if txn_type_choice == "1":
        ui.section_banner.heading_banner("INCOME")
    else:
        ui.section_banner.heading_banner("EXPENSE")

    #! transaction amt recording functionality
    txn_amt = txn_AmtRecorder()

    #! txn category recording
    categories_of_transaction
