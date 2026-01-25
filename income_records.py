print("=== Your Income Records ===")

income_amount = input(
    "Please input your income amount (Should be positive and numeric): \t"
)

# ? .isdigit(), isnumber() are only for strings, can be used to validate if user has entered numeric values in case of input() | i guess there's some difference between these methods, need to dig into it.

if not income_amount.isdigit():
    while not income_amount.isdigit():
        print("Attention User! Your input was non numeric ￣へ￣")
        income_amount = input("Re-enter your income, make sure input is numeric: \t")

# todo: Implement validation for negative & 0 inputs as well


print(
    "\n=== Please Enter Your Income Source ===\n1. Business \n2. Freelancing\n3. Salary \n4. Pocket Money \n5. Others "
)
category = input("Please input your income source: \t")
income_source = None

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
        income_source = "Other Sources"
print(income_source, income_amount)

# todo:  Implement category vlaidation
