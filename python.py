import time

def display_menu():
    """Display the menu options."""
    print("""
        1 - Check Balance
        2 - Withdraw Balance
        3 - Deposit Balance
        4 - View Transaction History
        5 - Exit
    """)

def handle_withdrawal(balance, history):
    """Handle withdrawal operation."""
    try:
        withdraw_amount = int(input("Please enter withdrawal amount: "))
        if withdraw_amount <= 0:
            print("Amount must be positive.")
        elif withdraw_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_amount
            history.append(f"Withdrew ${withdraw_amount:.2f}")
            print(f"${withdraw_amount} has been debited from your account.")
            print(f"Your updated balance is ${balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical amount.")
    return balance

def handle_deposit(balance, history):
    """Handle deposit operation."""
    try:
        deposit_amount = int(input("Please enter deposit amount: "))
        if deposit_amount <= 0:
            print("Amount must be positive.")
        else:
            balance += deposit_amount
            history.append(f"Deposited ${deposit_amount:.2f}")
            print(f"${deposit_amount} has been credited to your account.")
            print(f"Your updated balance is ${balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical amount.")
    return balance

def view_transaction_history(history):
    """Display the transaction history."""
    if not history:
        print("No transactions have been made.")
    else:
        print("Transaction History:")
        for transaction in history:
            print(transaction)

def atm_simulation():
    """Simulate an ATM transaction system."""
    print("Please insert Your CARD")
    time.sleep(5)  # Simulate card processing delay

    password = 1234  # Predefined ATM PIN
    balance = 5000    # Initial account balance
    max_attempts = 3  # Maximum attempts for entering PIN
    transaction_history = []  # List to store transaction history

    # PIN verification loop
    for attempt in range(max_attempts):
        try:
            pin = int(input("Enter your ATM PIN: "))  # Prompt user for ATM PIN
        except ValueError:
            print("Invalid input. Please enter a numerical PIN.")
            continue

        # Check if the entered PIN is correct
        if pin == password:
            break
        else:
            print("Wrong PIN. Please try again.")
            if attempt < max_attempts - 1:
                print(f"You have {max_attempts - attempt - 1} attempts left.")
            else:
                print("Too many incorrect attempts. Exiting.")
                return

    while True:
        display_menu()
        
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a numerical option.")
            continue

        if option == 1:
            print(f"Your current balance is ${balance:.2f}")

        elif option == 2:
            balance = handle_withdrawal(balance, transaction_history)

        elif option == 3:
            balance = handle_deposit(balance, transaction_history)

        elif option == 4:
            view_transaction_history(transaction_history)

        elif option == 5:
            print("Exiting. Thank you for using our ATM.")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    atm_simulation()
