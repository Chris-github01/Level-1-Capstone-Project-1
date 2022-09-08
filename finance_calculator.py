import math


# This function calculates simple interest return
def simple(p, r, t):
    a = round(p * (1 + (r / 100) * t), 2)
    print(f"\nYour total amount after {t} years will be R{a}")


# This function calculates compound interest return
def compound(p, r, t):
    a = round(p * math.pow((1 + (r / 100)), t), 2)
    print(f"\nYour total amount after {t} years will be R{a}")


# This function calculates bond repayment
def bond(I, p, n):
    i = (I / 12) / 100
    x = round((i * p) / (1 - math.pow((1 + i), -n)), 2)
    print(f"\nYour monthly bond repayment is R{x}")


# The user is asked to choose either 'investment' or 'bond'
calculator = input(f"""Choose either 'investment' or 'bond' from the menu below to proceed:

investment  - to calculate the amount of interest you'll earn on interest
bond        - to calculate the amount you'll have to pay on a home loan\n""").lower()

# The while loop is used to validate user input
while True:
    if calculator == "investment":  # Start of primary if statement calculates investment return
        amount = float(input("\nHow much money do you want to invest?\n"))
        rate = float(input("At what interest rate do you want to invest?\n"))
        period = float(input("How many years do you want to invest\n"))

        interest = input("\nHow do you want to invest? Simple or Compound?\n").lower()

        # Nested while loop is used to validate user input
        while True:

            # Nested if statement is used to calculate the two conditions, simple and compound interest
            if interest == "simple":
                simple(amount, rate, period)  # Call 'simple' function to display result
                break  # End of 'simple' loop

            elif interest == "compound":
                compound(amount, rate, period)  # Call 'compound' function to display result
                break  # End of 'compound' loop

            # End of nested if-statement
            # An error message will appear if an incorrect option is entered
            else:
                print("Incorrect option. Please try again.")

        # End of 'investment' loop
        break

    elif calculator == "bond":  # Primary elif statement calculates bond repayment
        present_value = float(input("\nWhat is the current value of your property?\n"))
        int_rate = float(input("At what interest rate do you want to pay off your bond?\n"))
        repay = float(input("How many months do you want to pay off your bond?\n"))

        # Call 'bond' function to display result
        bond(present_value, int_rate, repay)

        # End of 'bond' loop
        break

    # End of primary if statement
    # An error message will appear if an incorrect option is entered
    else:
        print("Incorrect option. Please try again.")

# References:
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_lists_sort.asp
# https://financeformulas.net/Loan_Payment_Formula.html
# https://www.calculatorsoup.com/calculators/financial/simple-interest
# https://www.calculatorsoup.com/calculators/financial/compound-interest
