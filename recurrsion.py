def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n-1)

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def power(a,b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print('Is it palindrome ', is_palindrome('racecar'))
