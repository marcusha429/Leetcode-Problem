class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        ans = []
        while left < right:
            if numbers[right] + numbers[left] < target:
                left+=1
            elif numbers[right] + numbers[left] > target:
                right-=1
            else:
                return [left+1, right+1] #be careful


            

        