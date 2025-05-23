class BankAccount:
    def __init__(self, owner, starting_balance=0):
        self.owner = owner
        self.balance = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Oops! Not enough funds.")
        elif amount <= 0:
            print("Withdraw amount must be positive!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")

    def check_balance(self):
        print(f"{self.owner}, your current balance is: {self.balance}")

# Example usage
if __name__ == "__main__":
    my_account = BankAccount("Faiyyaz", 1000)
    my_account.check_balance()
    my_account.deposit(500)
    my_account.withdraw(200)
    my_account.withdraw(1500)
