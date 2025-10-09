class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        for char_t in t:
            hashmap[char_t] = hashmap.get(char_t, 0) - 1
        if all(value == 0 for value in hashmap.values()):
            return True
        else:
            return False
