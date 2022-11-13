# -*- coding: utf-8 -*-
"""
Program: invoice.py

Programmer: Omar Shatrat

Date: 11/4/2022

Description: Object oriented program using classes and methods to complete invoices

"""
class Invoice:
# The invoice class can hold instances for different types of parts. For each part, the required parameters to include in an instance are part number, part description, quantity, and price.
  def __init__(self, part_num, part_desc, quantity, price):
      # Initializer/constructor taking in the required parameters. Requires non-negative numbers where applicable.
    self.part_num = str(part_num)
    self.part_desc = str(part_desc)
    
    if int(quantity) < 0:
      self.quantity = 'undefined'
    else:
      self.quantity = int(quantity)
    
    if float(price) < 0:
      self.price = 'undefined'
    else:
      self.price = float(price)
    
      # Mutator 'set' methods
  def set_part_number(self, part_num):
      # Gives client ability to alter part number parameter
      self.part_num = part_num
      return True
   
  def set_part_description(self, part_desc):
      # Gives client ability to alter part description parameter
      self.part_desc = part_desc
      return True
    
  def set_quantity(self, quantity):
      # Gives client ability to alter quantity parameter
      if int(quantity) < 0:
        return False
      else:
        self.quantity = int(quantity)
        return True
    
  def set_price(self, price):
      # Gives client ability to alter price parameter
      if float(price) < 0:
        return False
      else:
        self.price = float(price)
        return True
    
    # Accessor 'get' methods
  def get_part_number(self):
      # Gives client ability to retrieve part number parameter
      return self.part_num
    
  def get_part_description(self):
      # Gives client ability to retrieve part description parameter
      return self.part_desc
    
  def get_quantity(self):
      # Gives client ability to retrieve quantity parameter
      return self.quantity
    
  def get_price(self):
      # Gives client ability to retrieve price parameter
      return self.price
    
  def __str__(self):
      # Returns all parameter values to viewing
      return f'The part number is {self.part_num} \nThe description is {self.part_desc}\nThe quantity is {self.quantity} \nThe price is {self.price}\n'
    
  def calculate_invoice(self):
      # Calculates total price to be displayed on invoice
      return float(self.quantity) * float(self.price)

