class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        def backtracking(path):
            #base
            if len(path) == len(nums):
                ans.append(path[:])
                return ans
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtracking(path)
                    path.pop()
            
        backtracking([])
        return ans
