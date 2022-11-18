'''
Program: savingsaccount.py. 

Programmer: Omar Shatrat

Date: 11/17/2022

Description: Bank account subclass with methods.

'''

from account import Account

class SavingsAccount(Account):
    # Account subclass which inherits Account class
    def __init__(self, name, balance, int_rate):
        # Initializer for a bank account, takes name, balance, and interest rate
        super().__init__(name, balance)
        self.int_rate = int_rate
    
    def calculate_interest(self):
        # Calculates interest rate by multiplying rate and balance
        return float(self.int_rate * self.balance)
    
    def deposit(self, amt):
        # Allows user to deposit money
        super().deposit(amt)
    
    def withdraw(self, amt):
        # Allows user to withdraw money from their account, as long as it is positive and less than total balance
        super().withdraw(amt)
        
    def __str__(self):
        # Returns account holder and balance
        f = super().__str__()
        return f

