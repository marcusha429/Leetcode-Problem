class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] +=1

        return max((key for key, value in count.items() if value == 1), default = -1)
        