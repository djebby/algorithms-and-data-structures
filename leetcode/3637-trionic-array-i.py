# https://leetcode.com/problems/trionic-array-i/

from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if (len(nums) == 3 or nums[len(nums)-2] >= nums[len(nums)-1] or nums[0] >= nums[1]):
            return False
        
        # search for this pattern
        #   p  n-1
        #  / \ /
        # 0   q
        # inc -> dec -> inc

        p = False # p flag
        q = False # q flag
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]: # search for the (p)
                if p or q: return False
                else: p = True
            elif nums[i-1] > nums[i] and nums[i] < nums[i+1]: # search for the first (q)
                if not p or q: return False
                else: q = True

            if nums[i-1] == nums[i]: return False # if there are no strictly increasing or strictly decreasing

        return q and p

