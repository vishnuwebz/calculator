# main file to test your calculator package

from mini_projects.calculator import basic, advanced

# basic operations
print("Add:", basic.add(3, 5))
print("Subtract:", basic.subtract(8, 17))

# advanced operations
print("Multiply:", advanced.multiply(3, 14))
print("Divide:", advanced.divide(4, 2))
print("Divide by zero:", advanced.divide(10,0))

"""
output->

Add: 8
Subtract: -9
Multiply: 42
Divide: 2.0
Divide by zero: Error: Cannot divide by zero
"""
