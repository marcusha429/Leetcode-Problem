class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left = 0
        right = len(nums)-1
        right_ans = len(ans) -1

        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                ans[right_ans] = nums[right]**2
                right-=1
            else:
                ans[right_ans] = nums[left]**2
                left+=1
            right_ans-=1
        return ans
