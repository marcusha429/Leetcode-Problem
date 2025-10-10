class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        for letter in t:
            if letter not in s:
                return letter
            s.remove(letter)

            
            
            
                