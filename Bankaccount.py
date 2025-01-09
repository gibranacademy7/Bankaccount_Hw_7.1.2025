import random
import shelve
from datetime import datetime

class BankAccount:
    def __init__(self, account_id: int, full_name_owner: str, balance: float):
        self.account_id = account_id
        self.full_name_owner = full_name_owner
        self.balance = balance
        self.creation_time = datetime.now()  # Store the creation time when the account is created

    def __int__(self):
        return int(self.balance)

    def __str__(self):
        return f"BankAccount({self.account_id}): {self.full_name_owner} with balance: {self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount(account_id={self.account_id}, full_name_owner='{self.full_name_owner}', balance={self.balance}, creation_time={self.creation_time})"

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False

    def __ne__(self, other):
        if isinstance(other, BankAccount):
            return self.balance != other.balance
        return True

    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_account_id = random.randint(1000000, 9999999)  # Random account ID
            new_full_name = f"{self.full_name_owner} and {other.full_name_owner}"
            new_balance = self.balance + other.balance
            new_account = BankAccount(new_account_id, new_full_name, new_balance)
            return new_account
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            return self.balance - other.balance
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        return NotImplemented

    def __bool__(self):
        return self.balance != 0

    def __len__(self):
        delta = datetime.now() - self.creation_time
        return int(delta.total_seconds() // 60)  # Convert seconds to minutes and return as integer

b1 = BankAccount(8676230, "Wisam Gibran", 28000)
bg = BankAccount(6875533, "Hanan Assad", 28000)
b2 = BankAccount(5979982, "Arwa Spark", 79011)

print(bg == b1)  # True (same balance)
print(b1 != bg)  # False (same balance)
print(b1 > b2)   # False (28000 < 79011)
print(b1 < b2)   # True (28000 < 79011)

b3 = b1 + b2
print(b3)  # New account with a random account_id, combined balance (107011)

print(b2 - b1)  # 51,011 (subtracting balances)
print(b2 * b1)  # 2,212,308,000 (multiplying balances)

print(len(b1))  # Will output the number of minutes since the account was created

with shelve.open("bank_accounts.db") as shelf:
    shelf['b1'] = b1  # Store the b1 account object

with shelve.open("bank_accounts.db") as shelf:
    loaded_account = shelf['b1']
    print(f"Loaded account: {loaded_account}")  # Will print the stored account
