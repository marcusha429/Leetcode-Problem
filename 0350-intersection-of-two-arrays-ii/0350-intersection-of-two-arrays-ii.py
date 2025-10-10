class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        ans = []
        for num1 in nums1:
            hashmap[num1] = hashmap.get(num1,0) + 1

        for num2 in nums2:
            if hashmap.get(num2,0) > 0:
                ans.append(num2)
                hashmap[num2] -= 1
        return ans