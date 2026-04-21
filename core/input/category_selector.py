def get_transaction_category(choice):
    # ! NOTE: choice is that value which decides what transaction it is, if choice == 1 then it is income transaction else it is expense transction since we have binary logic here either it is income or it is expense, but I believe invalidating user inputs so for expense the choice value will be 2, but anyways any value which is not 1 will be considered as expense which is not the case as my previous step will never allow it
    # ? category data is stored in dictionaries allowing us to remove or edit categories in future should I implement an oboarding screen
    category_income = {
        1: "Business",
        2: "Freelancing",
        3: "Salary",
        4: "Pocket Money",
        5: "Others",
    }

    category_expense = {
        1: "Housing & Rent",
        2: "Loans & EMIs",
        3: "Investments",
        4: "Food & Groceries",
        5: "Transportation",
        6: "Bill & Utilities",
        7: "Health Care",
        8: "Shopping",
        9: "Education & Learning",
        10: "Travel & Hotel Bookings",
        11: "Entertainment",
        12: "Miscellaneous",
    }

    # ? making use of ternary operator to decide which dictionary to pick and ampping it to the argument provided so we don't have to use multiple if else statements in the code just to decide which dictionary to pick, making code shorter and honour DRY Principle

    map_category = category_income if choice == 1 else category_expense

    # ? prompting user for category message, based on argument, clearly ternary operators make code readbale aand clean.
    print(
        "Please Select Your Income Source"
        if choice == 1
        else "Where Was This Money Spent?"
    )

    # ? using for loop to extract keys and values from rhe dicitonary and printing them serially like a menu of choices, making use of .items() on dictionary mapped to the choice dictionary method and unpacking tupleusinf key, value in for loop
    for key, value in map_category.items():
        print(f"[{key}] {value}")

    # ? Prompting user to pick a transaction category as well as validating user inputs
    category_selection = input(
        f"Input your choice of category 1- {len(map_category)}: "
    )
    while (
        not category_selection.isdigit() or int(category_selection) not in map_category
    ):
        print("Invalid selection. Try again!")
        category_selection = input(
            f"Input your choice of category 1- {len(map_category)}: "
        )

    # ? the transction category will be retruned back to the caller
    return map_category[int(category_selection)]
