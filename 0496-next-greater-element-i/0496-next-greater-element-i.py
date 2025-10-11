class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                smaller_element = stack.pop()
                hashmap[smaller_element] = num2
            stack.append(num2)
        
        return [hashmap.get(num1, -1) for num1 in nums1]

            
