# Function to handle withdrawal
def handle_withdrawal(balance, min_withdrawal, max_withdrawal, withdrawal_amount):
    if withdrawal_amount < min_withdrawal or withdrawal_amount > max_withdrawal:
        return balance, f"Error: Withdrawal amount should be between {min_withdrawal} and {max_withdrawal}."
    elif withdrawal_amount > balance:
        return balance, "Error: Insufficient funds!"
    else:
        balance -= withdrawal_amount
        return balance, f"Transaction successful! Remaining balance: {balance}"

# Function to ask for another transaction
def ask_for_another_transaction():
    return input("Do you want to perform another transaction? (yes/no): ").lower() == "yes"

# Main program
def main():
    customer_balance = 1000
    min_withdrawal = 10
    max_withdrawal = 500
    print("Welcome to the ATM!")
    while True:
        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
        customer_balance, message = handle_withdrawal(customer_balance, min_withdrawal, max_withdrawal, withdrawal_amount)
        print(message)
        if not ask_for_another_transaction():
            break
    print("Thank you for using our ATM. Have a great day!")

if __name__ == "__main__":
    main()

