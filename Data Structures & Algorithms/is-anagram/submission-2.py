class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1,dict2 = {},{}
        for word in s:
            if word in dict1:
                dict1[word] = dict1.get(word) + 1
            else:
                dict1[word] = 1
        
        for word in t:
            if word in dict2:
                dict2[word] = dict2.get(word) + 1
            else:
                dict2[word] = 1
        
        return dict1 == dict2