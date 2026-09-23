class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in result.keys():
                return [result[complement],index]
            else:
                result[num] = index