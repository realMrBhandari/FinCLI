from tabulate import tabulate
from database.fetching_data import fetch_tranasctions

# ? tabulate specific formatting


def display_transactions():
    print(
        tabulate(
            fetch_tranasctions(),
            headers=[
                "Date",
                "Type",
                "Amt",
                "Category",
                "Mode",
                "Account",
                "Description",
            ],
            tablefmt="heavy_grid",
        )
    )
