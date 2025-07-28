def get_student_info(name, db):
    return db.get(name, "Not found.")

def most_common_word(words):
    word_count = {}
    if not words:
        return None
    for word in words:
        word_count[word] = word_count.get(word, 0)+1
    
    return max(word_count, key=word_count.get)

def swap_coordinates(point):
    if not isinstance(point, tuple) or len(point) != 2:
        raise ValueError("Input must be a tuple of two elements.")
    return (point[1], point[0])