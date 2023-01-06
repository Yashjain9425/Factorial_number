# n! = n * n-1 * n-2 * n-3.........1
# n! = n * (n-1)!


# method 1 by iterative method
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac *(i+1)
    return fac
number = int(input("Enter your number: "))
print(factorial_iterative(number))


# method 2 by recursive method
def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter your number: "))
print(factorial_recursive(number))