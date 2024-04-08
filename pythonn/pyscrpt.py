print("hello world")
import numpy as np

# Input the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Add the numbers using numpy
sum = np.add(num1, num2)

# Display the result
print("The sum of", num1, "and", num2, "is:", sum)