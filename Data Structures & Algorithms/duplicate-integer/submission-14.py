class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for index,num in enumerate(nums):
            if num in result:
                return True
            else:
                result[num] = index
            
        return False
        