# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_val = float('inf') # minimum value in the subarray nums[1:]
        sec_min_val = float('inf') # second minimum value in the subarray nums[1:]

        for num in nums[1:]:
            if num < min_val:
                sec_min_val = min_val
                min_val = num
            elif num < sec_min_val:
                sec_min_val = num
        
        return nums[0] + min_val + sec_min_val
