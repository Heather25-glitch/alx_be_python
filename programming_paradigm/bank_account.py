class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds are available. Returns True if successful, False otherwise."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False


def display_balance(self):
    """Print the current balance with two decimal places."""
    print(f"Current Balance: ${self.__account_balance:.2f}")
