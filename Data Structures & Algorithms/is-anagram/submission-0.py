from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        tList = list(t)

        if(Counter(sList) == Counter(tList)):
            return True
        return False