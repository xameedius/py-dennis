# You can check your balance - check_balance()
# winthdraw your balance - withdraw()
# Deposit funds - deposit()
# Main function - main()

def check_balance(balance):
    print(f"Your balance is {balance}")

def withdraw(balance):
    try:
        amount = float(input("Enter withdrawl amount: "))

        if amount < 0:
            raise ValueError("Withdrawl amount cannot be negative.")

        if amount > balance:
            raise Exception(f"Insufficient funds! Your balance is only {balance:.2f}")
        
    except ValueError as ve:
        print("ValueError", ve)

    except Exception as e:
        print("Error:", e)

    else:
        balance = balance - amount
        print(f"Withdrawl successful! {balance:.2f}")

    finally:
        print("Transaction Completed! ")

def deposit(balance):
    try:
        amount = float(input("Enter the deposit amount: "))

        if amount < 0:
            raise ValueError("The deposit amount cannot be negitive")
        
    except ValueError as ve:
        print("ValueError:",ve)

    else:
        balance = balance + amount

    finally:
        print("Transaction Completed")

    return balance

def main():
    # To test the functions
    balance = 1000.0 # Initial balance of the user

    while True:
        print("\nBanking System Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select an option (1-4):")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Exiting.. Thank you for using out banking system")
            break
        else:
            print("invalid choice: Please select a valid option.")

#Run the program
main()

