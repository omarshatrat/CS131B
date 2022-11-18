'''
Program: checkingaccount.py. 

Programmer: Omar Shatrat

Date: 11/17/2022

Description: Bank account subclass with methods.

'''

from account import Account

class CheckingAccount(Account):
    # Account subclass which inherits Account class
    def __init__(self, name, balance, fee):
              # Initializer for a bank account, takes name, balance, and transaction fee
        super().__init__(name, balance)
        self.fee = fee
    
    def withdraw(self, amt):
        # Allows user to withdraw money from their account, as long as it is positive and less than total balance
        super().withdraw( (amt + self.fee) )
  
    def deposit(self, amt):
        # Allows user to deposit money
        super().deposit( (amt - self.fee) ) 
    
    def __str__(self):
        # Returns account holder and balance
        f = super().__str__()
        return f


