"""
# Runtime : 32 ms
# Memory : 14.6 MB
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultDict = dict()
        for i in range(len(nums)):
            if nums[i] in resultDict:
                return [resultDict[nums[i]], i]

            resultDict[target - nums[i]] = i