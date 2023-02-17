# https://leetcode.com/problems/3sum/ (top-interview-questions)

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = list()

        for i in range(len(nums)-2):
            # we need to avoid any duplicate triplet
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                triplet_sum = nums[i] + nums[l] + nums[r]
                if triplet_sum < 0:
                    l += 1
                elif triplet_sum > 0:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    # we need to avoid any duplicate triplet
                    while nums[r] == nums[r+1] and l < r: 
                        r -= 1

        return triplets
