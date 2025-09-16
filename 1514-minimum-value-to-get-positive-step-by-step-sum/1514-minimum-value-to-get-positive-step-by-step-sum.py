class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        smallest_num = 0
        for num in nums:
            prefix_sum += num
            smallest_num = min(smallest_num, prefix_sum)
        return 1- smallest_num

            