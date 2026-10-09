# Encapsulation in Python is an OOP concept where you bundle data (attributes) 
# and the methods that operate on that data inside a class, while controlling 
# how that data is accessed or modified.

# For example, instead of allowing anyone to change a user's email directly, 
# you can use a property to validate it before updating it.

# Ex with no encapsulation

class BadBankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    

acc1 = BadBankAccount("shu", 500)

# print(acc1.balance)
acc1.balance = -1
# print(acc1.balance)

# above exmaple is bad as we are directly modifiying this balance
# without any cehcks or anything


# This is proper Encapsulation

# Internal data: _balance stores the account balance.

# Read access: curr_balance exposes the balance without allowing 
# assignment through the property.

# Controlled updates: deposit() and withdraw() validate transactions 
# before changing the balance.

# So the data is encapsulated and methods decates the rules how data can be acessed

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        
    @property
    def curr_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be less than 0")
        
        self._balance += amount
        
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insuficient Funds")
        
        if amount <= 0:
            raise ValueError("amount cannot be less than 0")
        

account = BankAccount(0.0)

print(account.curr_balance)
        