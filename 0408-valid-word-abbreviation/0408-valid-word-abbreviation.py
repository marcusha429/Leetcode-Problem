class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(abbr) and ptr2 < len(word):
            if abbr[ptr1].isdigit():
                if abbr[ptr1] == '0':
                    return False
                num = 0
                while ptr1 < len(abbr) and abbr[ptr1].isdigit():
                    num = num * 10 + int(abbr[ptr1])
                    ptr1 = ptr1 + 1
                ptr2 = ptr2 + num
            else:
                if abbr[ptr1] != word[ptr2]:
                    return False
                else:
                    ptr1 = ptr1 + 1
                    ptr2 = ptr2 + 1
        return ptr1 == len(abbr) and ptr2 == len(word)              



