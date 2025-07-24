# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

#My solution is brute force, which is not optimal.
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # ensure j != i and j > i
            if nums[i] + nums[j] == target:
                return [i, j]
            

#Optimal solution using a dictionary to store the indices of the numbers.
def twoSum(nums, target):
    num_map = {}  # to store number: index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index