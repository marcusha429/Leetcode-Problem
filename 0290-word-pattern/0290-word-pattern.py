class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def this_pattern(string):
            hashmap = {}
            position = []
            pos = 0
            for char in string:
                if char not in hashmap:
                    hashmap[char] = pos
                    pos += 1
                position.append(hashmap[char])
            return position
        word = s.split()
        return this_pattern(pattern) == this_pattern(word)
        