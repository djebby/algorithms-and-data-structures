# https://leetcode.com/problems/make-the-string-great/


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] != c and (stack[-1].upper() == c or stack[-1].lower() == c):
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
    

sol = Solution()
print(sol.makeGood('leEeetcode'))