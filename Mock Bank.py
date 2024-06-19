# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 20:13:18 2018

@author: Omar S
"""


userName = []
passwordList = []
balance = []

def main():
    
    print('***********************************')
    print("Menu options: \n1 Register account \n2 login with username and password \n3 exit")
    print('***********************************')
    option = eval(input("Choose an option from the menu:"))
    while option < 3 and option >= 1:
        if option == 1:
            register()
        elif option == 2:
            login()
        print('***********************************')
        print("Menu options: \n1 Register account \n2 login with username and password \n3 exit")
        print('***********************************')
        option = eval(input("Choose an option from the menu:"))
    print("Goodbye!")

 
def register():
    firstName = input("Enter your first name:")
    lastName = input("Enter your last name:")
    createUserName = firstName.lower() + lastName.lower()
    counter = 1
    temp = createUserName
    while temp in userName:
        if counter <= 1:
            print("Error username already exists.")
        temp = createUserName + str(counter)
        counter += 1
    userName.append(temp)
    print("Your username is:", temp)
     

    password = ""
    for ch in lastName:
        password = ch + password
    print("Your password is:", password)
    passwordList.append(password)
    
    newbalance = eval(input("Enter your balance amount:"))
    print("\n")
    balance.append(newbalance)
    mostValuable(userName.index(temp))
    
def login():
    username = input("Enter your username:")
    password = input("Enter your password:")
    index = -1
    try:
        index = userName.index(username)
    except ValueError:
        print("Username does not exist.", '\n')

    if index != -1:
        originalUserName = userName[index]
        originalPassword = passwordList[index]
        if originalPassword != password:
            print("Wrong login info", '\n')
        else:
            print("Login Successful!")
            print("Menu options: \n1 Withdraw \n2 Deposit\n")
            option = eval(input("Choose an option from the menu:"))
            if option == 1:
                withdraw = eval(input("Enter amount to withdraw:"))
                newbalance = balance[index]
                if withdraw > newbalance:
                    print("Withdraw denied!", '\n')
                else:
                    newbalance = newbalance - withdraw
                    print("Your new balance is:", newbalance)
                    balance.insert(index, newbalance)
            if option == 2:
                deposit = eval(input("Enter amount to deposit:"))
                newbalance = balance[index]
                newbalance = newbalance + deposit
                balance.insert(index, newbalance)
                print("Your new balance is:", newbalance, '\n')
                       

def mostValuable(userIndex): 
    index = 0
    maxIndex = 0
    maximum = balance[0]
    for newbalance in balance:
        if newbalance > maximum:
            maximum = newbalance
            maxIndex = index
        index += 1
    if maxIndex == userIndex:
        #print("The most valuable customer is:\n", userName[maxIndex])
        print(userName[maxIndex], "Thank you, you are a valued customer.\n")
    


main()

