# https://leetcode.com/problems/minimum-absolute-difference/

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')

        for i in range(1, len(arr)):
            min_diff = min(arr[i] - arr[i-1], min_diff)
        
        pairs = []
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) == min_diff:
                pairs.append([arr[i-1], arr[i]])
        
        return pairs

sol = Solution()
print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))