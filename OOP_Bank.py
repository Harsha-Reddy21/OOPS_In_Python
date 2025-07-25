class SavingsAccount:
    def __init__(self,account_number,holder_name,balance,interest_rate):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
        self.interest_rate=interest_rate

    def get_balance(self):
        return self.balance


    def deposit(self,amount):
        self.balance+=amount
        return f"Deposited {amount} to {self.account_number}. New balance: {self.balance}"

    def withdraw(self,amount):
        if amount>self.balance:
            return f"Insufficient balance in {self.account_number}. Current balance: {self.balance}"
        self.balance-=amount
        return f"Withdrawn {amount} from {self.account_number}. New balance: {self.balance}"


class CheckingAccount:
    def __init__(self,account_number,holder_name,balance,overdraft_limit):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
        self.overdraft_limit=overdraft_limit

    def get_balance(self):
        return self.balance


    def deposit(self,amount):
        self.balance+=amount
        return f"Deposited {amount} to {self.account_number}. New balance: {self.balance}"

    def withdraw(self,amount):
        if amount>self.balance+self.overdraft_limit:
            return f"Exceeds overdraft limit in {self.account_number}. Current balance: {self.balance}"
        self.balance-=amount
        return f"Withdrawn {amount} from {self.account_number}. New balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts=[]

    def add_account(self,account):
        self.accounts.append(account)


    def get_account_by_number(self,account_number):
        for account in self.accounts:
            if account.account_number==account_number:
                return account
        return None
    



savings_account=SavingsAccount("SA001","Alice",1000,0.02)
checking_account=CheckingAccount("CA001","Bob",500,100)


print(f"Savings Account:{savings_account}")
print(f"checking Account:{checking_account}")


print(f"Savings Account Balance:{savings_account.get_balance()}")
savings_account.deposit(200)
print(f"Savings Account Balance after deposit:{savings_account.get_balance()}")


withdraw_result=savings_account.withdraw(150)
print(f"Savings Account Withdrawal Result:{withdraw_result}")