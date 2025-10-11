class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap={}
        contain_odd = False
        count = 0
        for letter in s:
            hashmap[letter] = hashmap.get(letter,0) + 1
        for value in hashmap.values():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                contain_odd = True
        if contain_odd:
            count += 1
        return count
                