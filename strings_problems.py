def count_words(sentence):
    words = sentence.split()
    return len(words)

def most_frequent_char(sentence):
    sentence = sentence.lower()  # Normalize to lowercase
    frequency = {}
    for char in sentence:
        if char.isalpha():  # Count only alphabetic characters
            frequency[char] = frequency.get(char, 0) + 1
    if not frequency:
        return None
    return max(frequency, key=frequency.get)

def title_case(sentence):
    words = sentence.split()
    title_cased = ' '.join(word.capitalize() for word in words)
    return title_cased


print(most_frequent_char('Hello World! This is a test sentence.'))
print(title_case('hello world! this is a test sentence.'))