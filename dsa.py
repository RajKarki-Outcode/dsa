class Traveserse:
    def __init__(self, nums):
        self.nums = nums

    def traverse(self):
        output = [[self.nums[0]]]
        self.nums.pop(0)
        obj_len = len(self.nums)
        if not self.nums:
            print('The traverse of the list is:', output)
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





obj = Traveserse([1])
obj.traverse()