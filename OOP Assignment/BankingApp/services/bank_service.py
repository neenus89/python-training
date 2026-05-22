from models.account import Account, CurrentAccount, SavingsAccount

class BankService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_type: str, acc_num: str, name: str, initial_balance: float):
        if acc_num in self.accounts:
            print("Account number already exists.")
            return None
       
        if acc_type.lower() == "savings":
            account = SavingsAccount(acc_num, name, initial_balance)
            print(f"Savings Account created for {name}!")
        elif acc_type.lower() == "current":
            account = CurrentAccount(acc_num, name, initial_balance, CurrentAccount.OVERDRAFT_LIMIT)
            print(f"Current Account created for {name}!")
        else:
            print("Invalid account type.")
            return None
        
 
        self.accounts[acc_num] = account