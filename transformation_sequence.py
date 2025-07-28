# transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

from typing import List
from collections import defaultdict, deque

def find_ladders(begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
    word_set = set(word_list)
    if end_word not in word_set:
        return []
    
    layer = {begin_word: [[begin_word]]}
    while layer:
        new_layer = defaultdict(list)
        for word in layer:
            if word == end_word:
                return layer[word]  # Return all paths that reach the end_word
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        new_layer[new_word] += [j + [new_word] for j in layer[word]]
        
        word_set -= set(new_layer.keys())  # Remove words that have been processed
        layer = new_layer
    return []