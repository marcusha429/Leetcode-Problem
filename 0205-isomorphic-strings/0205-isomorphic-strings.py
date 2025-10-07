class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # def this_pattern(string):
        #     hashmap = {}
        #     for char in string:
        #         hashmap[char] = hashmap(char, 0) + 1
        #     print(hashmap)
        def this_pattern(string):
            hashmap = {}
            pattern = []
            _id = 0
            for char in string:
                if char not in hashmap:
                    hashmap[char] = _id
                    _id += 1
                pattern.append(hashmap[char])
            return pattern
        return this_pattern(s) == this_pattern(t)            

            