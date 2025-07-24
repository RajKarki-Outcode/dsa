# Given an integer x, return true if x is a palindrome, and false otherwise.


# My solution is to convert the integer to a string and check if it reads the same forwards and backwards.

def isPalindrome(x):
    x_str = str(x)  # Convert integer to string
    for i in range(len(x_str) // 2):
        if x_str[i] != x_str[len(x_str) - 1 - i]:
            return False
    return True

# Optimal solution using string slicing to check if the string is equal to its reverse.
def isPalindrome(x):
    return str(x) == str(x)[::-1]