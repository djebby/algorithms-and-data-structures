# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z' or letters[len(letters) - 1] <= target:
            return letters[0]
        l = 0
        r = len(letters) - 1

        while l < r:
            m = (l+r) // 2
            if target < letters[m]:
                r = m
            else:
                l = m + 1
        
        return letters[r] # letters[r] == letters[l] since after the while loop (l) should be equal to (r)
