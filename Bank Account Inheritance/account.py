'''
Program: account.py. 

Programmer: Omar Shatrat

Date: 11/17/2022

Description: Bank account superclass with methods.

'''
class Account:
    # Account superclass which other classes will inherit
  def __init__(self, name, balance):
      # Initializer for a bank account, takes name and balance
    self.name = str(name)
    self.balance = balance
  
  def withdraw(self, amt):
      # Allows user to withdraw money from their account, as long as it is positive and less than total balance
    if amt > self.balance:
      print("Withdrawal amount must be less than or equal to account balance.")
    elif amt < 0:
      print('Withdrawal amount must be positive.')
    else:
      self.balance -= amt
  
  def deposit(self, amt):
      # Allows user to deposit money
      self.balance += amt

  def __str__(self):
      # Returns account holder and balance
    return 'The account holder is '+ str(self.name) + ' and their balance is $' + str(self.balance)

