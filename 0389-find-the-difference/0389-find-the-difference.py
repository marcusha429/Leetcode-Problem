class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s = list(s)
        # for letter in t:
        #     if letter not in s:
        #         return letter
        #     s.remove(letter)

        hashmap = {}
        for letter_s in s:
            hashmap[letter_s] = hashmap.get(letter_s, 0) + 1

        for letter_t in t:
            hashmap[letter_t] = hashmap.get(letter_t, 0) - 1
            if hashmap[letter_t] < 0:
                return letter_t

            
            
            
                