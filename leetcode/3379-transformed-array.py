# https://leetcode.com/problems/transformed-array/

from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)

        for i in range(0, len(nums)):
            if nums[i] > 0:
                result[i] = nums[(i+nums[i]) % len(nums)]
            elif nums[i] < 0:
                lsteps = abs(nums[i]) % len(nums)
                result[i] = nums[-(lsteps - i)]
            else:
                result[i] = 0
            
        return result
