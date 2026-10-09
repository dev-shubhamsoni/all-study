# Static Methods - stored i class same as sintance methods

# Astatic method in python is a mehtod hatbelongs to aclass itself
# rather than any isntance of the class

# To define we use @staticmethod decorator

# Use a static method when a function is logically related to a 
# class but doesn't need the object's or class's data.

# For example, in a User class, you might have a method to 
# validate an email format

class BankAccount:
    MIN_BALANCE = 0
    
    def __init__(self, name, acc_balance):
        self.name = name
        self.acc_balance = acc_balance
        
    def deposit(self,amount):
        if self._amount_check(amount):
            self.acc_balance += amount
            self.__log_transaction("deposit", amount)
    
    @staticmethod
    # no self required in static methods
    def check_intrest_rate(rate):
        return rate >= 0 and rate <= 5
    
    # Protected method - only to be used in class or sub classes.
    def _amount_check(self, amount):
        return amount > 0
    
    # Private methods - not allowed to access outside of class.
    def __log_transaction(self, transaction_type, amount):
        print(f"Loggin {transaction_type} of {amount}. New Balance: {self.acc_balance}")
    
    
    
    
acc1 = BankAccount("Shu", 500)
acc1.deposit(0)
print(BankAccount.check_intrest_rate(5))