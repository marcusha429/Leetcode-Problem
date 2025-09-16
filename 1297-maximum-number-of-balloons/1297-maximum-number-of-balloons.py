class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        balloon_hashmap = defaultdict(int)
        text_hashmap = defaultdict(int)
        count = 0
        for char in word:
            balloon_hashmap[char] += 1

        for character in text:
            text_hashmap[character] += 1
        
        ans = float('inf')
        for ch in balloon_hashmap:
            ans = min(ans, text_hashmap[ch] // balloon_hashmap[ch])
        return ans

