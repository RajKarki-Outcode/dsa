nums = [1,2,3]
k = 3
index = 0
output = []
sub_array = []
for index in range(len(nums)):
    if nums[index] > k:
        index += 1
        continue
    sub_array.append(nums[index])
    if sum(sub_array) == k:
        output.append(sub_array)
        sub_array = []
    elif sum(sub_array) < k :
        continue
    else:
        sub_array = []
        index += 1
    
    

print(sub_array) 

print(output) 
