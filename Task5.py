# Task 5: Factorial Calculation

factorial =int(input("Enter a number: "))
def factorial_function(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_function(n - 1)

result = factorial_function(factorial)
print("Factorial of Given number:",result)