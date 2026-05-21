# ! All input modules from core/input
from core.input.amount_input import txn_AmtRecorder
from core.input.transaction_type_input import get_txn_type
from core.input.category_selector import get_transaction_category
from core.input.date_input import txn_DateRecorder
from core.input.metadata_input import txn_MetadataRecorder
from database.insert_statement import append_transaction

# TODO [2]: fix function naming develop a pattern


def record_transactions():
    # ?Basic Flow of programme:  [transaction amount] --> [type of transaction (income/expense?)] --> [transaction category] --> [transaction date] --> [transaction metadata (account, mode, node)]
    transaction_amount = txn_AmtRecorder()

    transaction_type = get_txn_type()

    transaction_category = get_transaction_category(int(transaction_type))

    transaction_date = txn_DateRecorder()

    transaction_mode, transaction_account, transaction_note = (
        txn_MetadataRecorder()
    )  # ? this function returns tuple so unpacking tuple

    append_transaction(
        txn_date=transaction_date,
        txn_type="CREDIT" if transaction_type == "1" else "DEBIT",
        txn_amount=transaction_amount,
        txn_category=transaction_category,
        txn_account=transaction_account,
        txn_mode=transaction_mode,
        txn_note=transaction_note,
    )
