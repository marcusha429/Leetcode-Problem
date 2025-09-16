class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = suffix_sum = total = count = 0
        for num in nums:
            total += num
        for ptr in range(len(nums) -1):
            prefix_sum += nums[ptr]
            suffix_sum = total - prefix_sum
            if(prefix_sum >= suffix_sum):
                count+=1
        return count
            

        
        
        