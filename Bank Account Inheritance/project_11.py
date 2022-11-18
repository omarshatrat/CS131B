'''
Program: project_11.py. 

Programmer: Omar Shatrat

Date: 11/17/2022

Description: Tests all methods from previous classes

'''

from account import Account
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

print('\nAccount \n')

acc1 = Account('Omar Shatrat', 100) 

print('Initial Print:')
print(acc1.__str__())
acc1.withdraw(3) 
acc1.deposit(19)

print('\nNew Print (after withdrawing 3, depositing 19, withdrawing 200, and withdrawing -20):')
print(acc1.__str__())
acc1.withdraw(200)
acc1.withdraw(-20)

print('\nSavings Account \n')

print('Initial Print:')
acc2 = SavingsAccount('John Doe', 59, .02)
print(acc2.__str__())
acc2.withdraw(3) 
acc2.deposit(19)
print('\nNew Print (after withdrawing 3, depositing 19, withdrawing 200, and withdrawing -20, and adding 2% interest):')
print(acc2.__str__())
acc2.withdraw(200)
acc2.withdraw(-20)
print('The interest rate is:', str(acc2.calculate_interest()) + '%'  )
print('The balance with interest is:', str( (1 + (acc2.calculate_interest()/100) ) * acc2.balance ) )

print('\nChecking Account \n')
print('Initial Print:')
acc3 = CheckingAccount('Omar Doe', 157, 3)
print(acc3.__str__())
acc3.withdraw(3) 
acc3.deposit(19)
print('\nNew Print (after withdrawing 3, depositing 19, withdrawing 200, and withdrawing -20 with a $3 fee):')
print(acc3.__str__())
acc3.withdraw(200)
acc3.withdraw(-20)

'''Sample run

Account 

Initial Print:
The account holder is Omar Shatrat and their balance is $100

New Print (after withdrawing 3, depositing 19, withdrawing 200, and withdrawing -20):
The account holder is Omar Shatrat and their balance is $116
Withdrawal amount must be less than or equal to account balance.
Withdrawal amount must be positive.

Savings Account 

Initial Print:
The account holder is John Doe and their balance is $59

New Print (after withdrawing 3, depositing 19, withdrawing 200, and withdrawing -20, and adding 2% interest):
The account holder is John Doe and their balance is $75
Withdrawal amount must be less than or equal to account balance.
Withdrawal amount must be positive.
The interest rate is: 1.5%
The balance with interest is: 76.12499999999999

Checking Account 

Initial Print:
The account holder is Omar Doe and their balance is $157

New Print (after withdrawing 3, depositing 19, withdrawing 200, and withdrawing -20 with a $3 fee):
The account holder is Omar Doe and their balance is $167
Withdrawal amount must be less than or equal to account balance.
Withdrawal amount must be positive.

'''