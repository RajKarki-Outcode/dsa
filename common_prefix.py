#My solution
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return prefix
            prefix += char

        return prefix

#Optimal Solution
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # Remove last char
                if not prefix:
                    return ""
        
        return prefix