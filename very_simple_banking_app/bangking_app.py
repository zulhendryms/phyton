def show_balance(balance):
    print("\n--- Your Current Balance ---")
                    print(f"Balance: ${balance:.2f}")
    print("-----------------------------\n")

def deposit():
    print("\n--- Deposit Funds ---")
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return 0
        return amount
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return 0

def withdraw(balance):
    print("\n--- Withdraw Funds ---")
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Error: Insufficient funds.")
            return 0
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return 0
        return amount
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return 0

def display_menu():
    		print("\n--- Banking Program ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("-----------------------")

def main():
    balance = 0
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("\nThank you for using the Banking Program!")
            break
        else:
            print("Error: Invalid choice. Please select an option between 1 and 4.")

if __name__ == '__main__':
    main()
