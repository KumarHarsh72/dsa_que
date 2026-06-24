class Solution:
    def balancedStringSplit(self, s: str) -> int:
        direction=0
        ans=0
        for i in s:
            if i=='R':
                direction+=1
            else:
                direction-=1
            if direction == 0:
                ans+=1
        return ans
        