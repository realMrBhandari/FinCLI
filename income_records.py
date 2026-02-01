# ! Input Amount Code
print("=== Your Income Records ===")
income_amount = input(
    "Please input your income amount (Should be positive and numeric): \t"
)
if not income_amount.isdigit():
    while not income_amount.isdigit():
        print("Attention User! Your input was non numeric ￣へ￣")
        income_amount = input("Re-enter your income, make sure input is numeric: \t")
# todo: Implement validation for negative & 0 inputs as well

# todo: A type conversion is needed here, the user input which is string is needed to be converted into a numeric type once input for income amount is validated.

# todo: implement the industrial level of recording money, i guess money is not recorded in floating points, but whatever system it is money will be stored in that method.

# ! Income Source Section
income_source = None
print(
    "\n=== Please Enter Your Income Source ===\n1. Business \n2. Freelancing\n3. Salary \n4. Pocket Money \n5. Others "
)
category = input("Please input your income source: \t")
valid_inputs = ["1", "2", "3", "4", "5"]
while category not in valid_inputs:
    print("Your input was invalid:")
    category = input("Please re-enter your income source: \t")
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
        income_source = input("Please specify your source:\t")
        # TODO ONE MORE CONDITION SHOULD BE IMPLEMENTED HERE WHERE THERE SHOULD BE A DEFAULT CASE IN CASE USER DOES NOT PROVIDE ANY INCOME SOURCE


# ! All this can be wrapped in a function and and can be called over and over again from the FinCLI menu itself
