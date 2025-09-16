class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = {}
        count = 0
        for i in range(len(sentence)):
            if sentence[i] not in hashmap:
                hashmap[sentence[i]] = i
        return len(hashmap) == 26

        