# -*- coding: utf-8 -*-
"""
Program: project9.py

Programmer: Omar Shatrat

Date: 11/4/2022

Description: Calls of methods and classes created in invoice.py

"""

import invoice

inv1 = invoice.Invoice('33', 'wrench', 4, 10.0)
inv2 = invoice.Invoice('44', 'hammer', 7, 15)
inv3 = invoice.Invoice('55', 'nails', 9, 2)
inv4 = invoice.Invoice('66', 'paint', 2, 20)

print('ORIGINAL OUTPUT:\n')

print(inv1.__str__())
print(inv2.__str__())
print(inv3.__str__())
print(inv4.__str__())

inv1.set_price(12)
inv2.set_part_number('1221')
inv3.set_part_description('stainless steel nails')
inv4.set_quantity(11)

print('MUTATED OUTPUT:\n')

print(inv1.__str__())
print(inv2.__str__())
print(inv3.__str__())
print(inv4.__str__())

print('ACCESSOR CALLS:\n')

print('Inv1 Price:', inv1.get_price())
print('Inv2 Part Number:', inv2.get_part_number())


'''Sample output

ORIGINAL OUTPUT:

The part number is 33 
The description is wrench
The quantity is 4 
The price is 10.0

The part number is 44 
The description is hammer
The quantity is 7 
The price is 15.0

The part number is 55 
The description is nails
The quantity is 9 
The price is 2.0

The part number is 66 
The description is paint
The quantity is 2 
The price is 20.0

MUTATED OUTPUT:

The part number is 33 
The description is wrench
The quantity is 4 
The price is 12.0

The part number is 1221 
The description is hammer
The quantity is 7 
The price is 15.0

The part number is 55 
The description is stainless steel nails
The quantity is 9 
The price is 2.0

The part number is 66 
The description is paint
The quantity is 11 
The price is 20.0

ACCESSOR CALLS:

Inv1 Price: 12.0
Inv2 Part Number: 1221

'''