class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashmap = {6: 9, 9: 6, 8: 8, 0: 0, 1: 1}
        inter = int(num)
        after_reverse = ""

        if inter == 0: 
            return True

        while inter != 0:
            digit = inter % 10
            if digit not in hashmap:
                return False
            else:
                after_reverse += str(hashmap[digit]) 
                inter = inter // 10
        return after_reverse == num