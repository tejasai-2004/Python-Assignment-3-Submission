# Python-Assignment-3-Submission


Task 1: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.


 Program:

# Task 5: Factorial Calculation

factorial =int(input("Enter a number: "))
def factorial_function(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_function(n - 1)

result = factorial_function(factorial)
print("Factorial of Given number:",result)


Expected Output:

Enter a number: 5
Factorial of Given number: 120



Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

Program:

#math module calculations

#square root of a number
a=int(input("Enter a number: "))
import math 
square_root = math.sqrt(a)
print("square root of :",square_root)

#natuaral logarithm of a number
natural_log = math.log(a)
print("Natural logarithm is:", natural_log)

#sine of a number
print("Sine of the angle is:",(math.sine(a)))


 Expected Output:
Enter a number: 25
square root of : 5.0
Natural logarithm is: 3.2188758248682006
Sine of the angle is: -0.13235175009777303
 
