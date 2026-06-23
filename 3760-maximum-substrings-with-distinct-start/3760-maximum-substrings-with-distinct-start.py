class Solution:
    def maxDistinct(self, s: str) -> int:
        p=""
        for i in s:
            if i not in p:
                p+=i
        return len(p)
        