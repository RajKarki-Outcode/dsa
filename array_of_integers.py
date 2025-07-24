# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).


## My solution is to use a binary search to find the smallest divisor.
import math

def smallestDivisor(nums, threshold):
    i = 1
    while True:
        total = sum(math.ceil(num / i) for num in nums)
        if total <= threshold:
            return i
        i += 1

# Optimal solution using binary search to find the smallest divisor.
def smallestDivisor(nums, threshold):
    left, right = 1, max(nums)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(math.ceil(num / mid) for num in nums)
        
        if total <= threshold:
            answer = mid  # try smaller divisor
            right = mid - 1
        else:
            left = mid + 1  # need bigger divisor
            
    return answer