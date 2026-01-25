# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set: return num
            num_set.add(num)
