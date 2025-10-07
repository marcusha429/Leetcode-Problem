class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = defaultdict(int)
        for num in nums:
            hashtable[num] += 1
            if hashtable[num] > len(nums)/2:
                return num