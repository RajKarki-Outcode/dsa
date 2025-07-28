def clean_string(s):
    s = s.strip().lower()
    if 'python' in s:
        s = s.replace('python', 'Python')
    return s

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    s = s.lower().strip()
    return s == s[::-1]
print(clean_string(" heLlo, python! ")) 
print(count_vowels(" heLlo, python! ")) 
print(is_palindrome(" Racecar")) 
