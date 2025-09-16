class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        numberOfOdd = 0
        count = 0
        for num in nums:
            if num%2 == 1:
                numberOfOdd += 1
            if numberOfOdd - k in hashmap:
                count += hashmap[numberOfOdd - k]
            hashmap[numberOfOdd] += 1
        return count