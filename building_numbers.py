# -*- coding: utf-8 -*-
"""
Program: building_numbers.py. 

Programmer: Omar Shatrat

Date: 12/05/2022

Description: Program populates dictionary, writes it to a file, then reads the file in and displays it

"""

# CS131B Project 13
# I promise that I understand the code I am submitting well enough to write similar code on a test.



class DictionaryFileManager:
    # Contructor here initializes an instance by taking a filename
    def __init__(self, filename):
        self.filename = filename
    
    # The function takes a dictionary as a parameter and writes it to a file
    def write_dictionary_to_file(self, dictionary):
        with open('dictionary.txt', 'w') as f:
            for key, value in dictionary.items():
                f.write(f"{key}:{value}\n")
    
    # Function reads a file, writes its attributes to a dictionary, and that dictionary is the return value
    def read_dictionary_from_file(self, filename):
        mydict = {}
        try:
            with open(filename, 'r') as f:
                for line in f:
                    key, value = line.strip().split(":")
                    mydict[key] = value
        except IOError:
            return {}
        return mydict
    
def main():
    go = 1
    building_numbers = {}

    while go == 1:
        # This loop populates the dictionary until the user decides to stop
        name = input('Enter new name: ')
    
        if name != '':
            bldng = input('Enter new building number: ')
    
        if name != '' and bldng != '':
            building_numbers[name] = int(bldng)
    
        lookup = input('Enter name to look up: ')
        if lookup in list(building_numbers.keys()):
            print('Building number:', building_numbers[lookup])
    
        go = int(input('0 to quit, 1 to enter again '))
    
    # The main program Writes a dictionary to a file, then reads that file in and displays the dictionary therein
    manager = DictionaryFileManager('dictionary.txt')
    manager.write_dictionary_to_file(building_numbers)
    dict1 = manager.read_dictionary_from_file('dictionary.txt')
    print(dict1)

main()


'''Sample run

Enter new name: omar

Enter new building number: 1

Enter name to look up: 

0 to quit, 1 to enter again 1

Enter new name: adam

Enter new building number: 2

Enter name to look up: omar
Building number: 1

0 to quit, 1 to enter again 0
{'omar': '1', 'adam': '2'}

A FILE IS ALSO WRITTEN WHICH CONTAINS THIS DICTIONARY

'''
