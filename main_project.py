import math_operations

  # Test the module functions
a = 10
b = 5

print(f"The sum of {a} and {b} is: {math_operations.add(a, b)}")
print(f"The difference between {a} and {b} is: {math_operations.subtract(a, b)}")
print(f"The product of {a} and {b} is: {math_operations.multiply(a, b)}")
print(f"The division of {a} by {b} is: {math_operations.divide(a, b)}")

  # division by zero 
b = 0
print(f"The division of {a} by {b} is: {math_operations.divide(a, b)}")