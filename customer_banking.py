# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main(savings_balance,cd_balance, interest_rate, months):
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter your savings balance:")), 
    interest_rate = float(input('Enter the interest rate for the savings account (%): ')), 
    months = float(input("Enter the number of months for the savings account: "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_balance, interest_earned = create_savings_account(savings_balance, interest_rate, months)
    

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"Updated savings account balance with interest earned: ${updated_balance:.2f}")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter your CD balance: "))
    cd_interest = float(input("Enter the CD interest rate: "))
    cd_months = int(input("Enter the number of months for the CS: "))


    # Call the create_cd_account function and pass the variables from the user.
    interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("Interest earned on the CD account: ${:.2f}".format(interest_earned))
    print("Updated CD account balance with interest earned: ${:.2f}".format(updated_balance))

    # Call the main function.
    main()
    return interest_earned, updated_balance 