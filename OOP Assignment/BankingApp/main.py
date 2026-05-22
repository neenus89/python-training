from services.bank_service import BankService

def main():
    bank_service = BankService()

    while True:
        print("\nWelcome to the Banking App!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc_type = input("Enter account type (Savings/Current): ")
            acc_num = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank_service.create_account(acc_type, acc_num, name, initial_balance)

        elif choice == '2':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if acc_num in bank_service.accounts:
                bank_service.accounts[acc_num].deposit(amount)
                print(f"Deposited {amount} to account {acc_num}.")
            else:
                print("Account not found.")

        elif choice == '3':
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if acc_num in bank_service.accounts:
                try:
                    bank_service.accounts[acc_num].withdraw(amount)
                    print(f"Withdrew {amount} from account {acc_num}.")
                except Exception as e:
                    print(e)
            else:
                print("Account not found.")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            if acc_num in bank_service.accounts:
                balance = bank_service.accounts[acc_num].get_balance()
                print(f"Balance for account {acc_num}: {balance}")
            else:
                print("Account not found.")

        elif choice == '5':
            print("Thank you")
            break

        else:
            print("Invalid choice. Please try again.")

main()