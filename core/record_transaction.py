# ! All input modules from core/input
from core.input.amount_input import txn_AmtRecorder
from core.input.transaction_type_input import get_txn_type
from core.input.category_selector import get_transaction_category
from core.input.date_input import txn_DateRecorder
from core.input.metadata_input import txn_MetadataRecorder
from tabulate import tabulate

# TODO [2]: fix function naming develop a pattern


def record_transactions():
    # ?Basic Flow of programme:  [transaction amount] --> [type of transaction (income/expense?)] --> [transaction category] --> [transaction date] --> [transaction metadata (account, mode, node)]
    txn_amount = txn_AmtRecorder()

    txn_type = get_txn_type()

    txn_category = get_transaction_category(int(txn_type))

    txn_date = txn_DateRecorder()

    txn_mode, txn_account, txn_note = (
        txn_MetadataRecorder()
    )  # ? this function returns tuple so unpacking tuple
