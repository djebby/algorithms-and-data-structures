# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix = [0] # B's counts before the current index
        suffix = [0] # A's counts after the current index

        for i in range(0, n):
            prefix.append(prefix[-1] + (1 if s[i] == 'b' else 0))
        
        for i in range(n-1, -1, -1):
            suffix.append(suffix[-1] + (1 if s[i] == 'a' else 0))
        
        prefix.pop()
        suffix.pop()
        suffix.reverse()

        min_deletions = float('inf')
        for i in range(0, n):
            min_deletions = min(min_deletions, (prefix[i] + suffix[i]))

        return min_deletions


