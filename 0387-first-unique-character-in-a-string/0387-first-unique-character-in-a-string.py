class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for letter in s:
            hashmap[letter] = hashmap.get(letter,0) + 1
        for _id, letter in enumerate(s):
            if hashmap[letter] == 1:
                return _id
        return -1