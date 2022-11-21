import math

# Display program usage. The user must type "investment" or "bond"
print("Choose either \"investment\" or \"bond\" from the menu below to proceed:")
print("\ninvestment\t-\tto calculate the amount of interest you'll earn on your investment")
print("bond\t\t-\tto calculate the amount you'll have to pay monthly on a home loan")

user_choice = input("\n").lower()

# Handle incorrect input.
if user_choice != "bond" and user_choice != "investment":
    print("\n!!!Wrong input. Please type either \"investment\" or \"bond\"!!!\n")

# Ask the user for more details
if user_choice == "investment":
    # To calculate the investment profits the program needs the initial deposit amount, the annual interest rate and
    # the number of years of investment.
    deposit = float(input("\nEnter the amount of money you wish to deposit (digits only):\t£"))
    interest_rate = float(input("Enter the interest rate percentage (digits only):\t\t")) / 100
    years = int(input("Enter the number of years you plan on investing:\t\t"))

    # Finally, the user will have to specify if it is simple or compound interest.
    interest = input("Choose \"simple\" or \"compound\" to specify the type of interest:\t").lower()

    # Handle incorrect input
    if interest != "simple" and interest != "compound":
        print("\n!!!Wrong input. Please type either \"simple\" or \"compound\"!!!\n")

elif user_choice == "bond":
    # To calculate the monthly repayment of a mortgage the program need the house value, the annual interest rate (which
    # will be divided monthly) and the length of the mortgage in months.
    house_value = float(input("\nEnter the amount to borrow (digits only):\t£"))
    interest_rate = float(input("Enter the interest rate percentage (digits only):\t")) / 12 / 100
    months = int(input("Enter how many months it will take to repay the bond:\t"))

# Finally calculate the result. I chose to perform this operation in a separate if-statement to avoid
# further nesting and keep the code tidier.
if user_choice == "investment":
    # Calculate simple investment
    if interest == "simple":
        total_amount = round(deposit * (1 + interest_rate * years), 2)
        print(f"\n=== Your end balance will be £{total_amount} You'll have earned £{round(total_amount - deposit, 2)} in interest. ===\n")
    
    # Calculate compound investment
    if interest == "compound":
        total_amount = round(deposit * math.pow((1 + interest_rate), years), 2)
        print(f"\n=== Your end balance will be £{total_amount} You'll have earned £{round(total_amount - deposit, 2)} in interest. ===\n")

elif user_choice == "bond":
    # Calculate mortgage repayment
    total_amount = round((interest_rate * house_value) / (1 - math.pow(1 + interest_rate, (months * -1))), 2)
    print(f"\n=== Your monthly payment is going to be £{total_amount} ===\n")
