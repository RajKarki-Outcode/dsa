# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# i dont need the solution i am not understanding the question like what it is asking can you describe this and show me more examples

#My solution is to use a queue to traverse the
class Traveserse:
    def __init__(self, nums):
        self.nums = nums

    def traverse(self):
        output = [[self.nums[0]]]
        self.nums.pop(0)
        obj_len = len(self.nums)
        if not self.nums:
            return
        
        level_elem = []
        lim = 2
        for i in self.nums:
            print(lim)
            if lim == 0:
                print('The level is complete', len(output))
                lim = (len(output)+1) * 2
                output.append(level_elem)
                level_elem = []
            level_elem.append(i)
            lim -= 1
            if i is self.nums[-1]:
                output.append(level_elem)
                break
        print('The traverse of the list is:', output)





obj = Traveserse([1,2,3,4,5,6,7,8,9])
obj.traverse()

#Optimal solution using queue to traverse the list. This solution uses a queue to keep track of the
from math import pow, ceil

class Traverse:
    def __init__(self, nums):
        self.nums = nums

    def traverse(self):
        output = []
        index = 0
        level = 0

        while index < len(self.nums):
            level_size = int(pow(2, level))  # number of elements in this level
            level_elements = self.nums[index : index + level_size]
            output.append(level_elements)
            index += level_size
            level += 1

        print('The traverse of the list is:', output)
