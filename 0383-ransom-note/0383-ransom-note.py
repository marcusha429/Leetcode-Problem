class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for note in magazine:
            hashmap[note] = hashmap.get(note,0) + 1
        for char in ransomNote:
            if hashmap.get(char, 0) == 0:
                return False
            hashmap[char] -= 1
        return True