class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        sList = list(s)
        palin = sList[::-1]

        if(sList == palin):
            return True
        return False