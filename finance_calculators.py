# Capstone Project 1

# import math is used to use the function math.pow which is stored in the Python library.
# This function will be used in the below calculations.
import math

# The tab function \t is used to create an equal space on the output
# The new line separator \n is used to move the string to a new line
print("\nChoose either 'investment' or 'bond' from the menu below to proceed:")
print("\ninvestment\t - to calculate the amount of interest you'll earn on interest")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan")

# The .lower() function is used to make the input name all lowercase to account for how
# the user enters the name of the calculator, i.e Bond vs BOND
# The input() function is used to store all value needed for the calculations
calculator = input("\nWhich calculator do you want to open? ").lower()

# Start of primary if statement
# 'deposit' and 'int_rate' are stored as float values as it can have decimal places
# 'num_years' is stored as an integer value
if calculator == "investment":
    deposit = float(input("\nHow much money do you want to invest in R? "))
    int_rate = float(input("At what interest rate (in percentage) do you want to invest? "))
    num_years = int(input("How many years do you want to invest? "))

    # The .lower() function is used to make 'interest' all lowercase to account for how
    # the user enters the name, i.e Simple vs SIMPLE
    interest = input("How do you want to invest? Simple or Compound? ").lower()
    r = int_rate/100

    # Nested if statement under investment calculator is used to calculate the two
    # conditions, simple and compound interest
    if interest == "simple":
        tot_invest = round((deposit * (1 + r * num_years)), 2)

        print("\nYour total amount after {} years will be R{}".format(num_years, tot_invest))

    else:
        tot_invest = round((deposit * math.pow((1 + r), num_years)), 2)

        print("\nYour total amount after {} years will be R{}".format(num_years, tot_invest))
    # End of nested if statement

# Continue primary if statement
# The elif is used since there are 3 conditions to be checked
# 'present_value' and 'int_rate' is stored as float values as it can have decimal places
# 'months_repay' is stored as an integer value
elif calculator == "bond":
    present_value = float(input("\nWhat is your present value of your property? "))
    int_rate = float(input("At what interest rate (in percentage) do you want to pay off your bond? "))
    months_repay = int(input("How many months will you payoff your property? "))

    # Values 'i' and 'n' is calculated upfront to simplify the 'bond_repay' formula
    i = (int_rate/12)/100
    n = -1 * months_repay
    bond_repay = round(((i * present_value) / (1 - math.pow((1 + i), n))), 2)

    print("\nYour monthly bond repayment is R{}".format(bond_repay))

# End of primary if statement
else:
    print("\nYou did not select a valid calculator. \nPlease select 'Investment' or 'Bond'.")

# References:
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_lists_sort.asp
# https://financeformulas.net/Loan_Payment_Formula.html
# https://www.calculatorsoup.com/calculators/financial/simple-interest
# https://www.calculatorsoup.com/calculators/financial/compound-interest
