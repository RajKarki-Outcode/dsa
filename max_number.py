def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num

    return min_num

def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    if not numbers:
        return 0,0
    
    for num in numbers:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

def list_reverse(numbers):
    if not numbers:
        return []
    return numbers[::-1]

sample = [3, 5, 2, 9, 1]
print('Max value: ',find_max(sample))  
print('Min value: ',find_min(sample)) 
even, odd = count_even_odd(sample)
print(f"Even count: {even}, Odd count: {odd}") 
print('Reversed value: ',list_reverse(sample))  