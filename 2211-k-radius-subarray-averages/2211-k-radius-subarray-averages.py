class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_len = 2*k+1
        ans = [-1]*len(nums)
        prefix_sum=0
        middle_avg = k
        #instantly put -1 for this condition
        if window_len > len(nums):
            return [-1]*len(nums)

        for i in range(window_len):
            prefix_sum += nums[i]
            ans[middle_avg] = prefix_sum // window_len

        for window in range(window_len, len(nums)):
            #shift the window by +/- and shift the center and average
            prefix_sum = prefix_sum - nums[window - window_len]
            prefix_sum = prefix_sum + nums[window]
            ans[window - k] = prefix_sum // window_len
        return ans

         
                

