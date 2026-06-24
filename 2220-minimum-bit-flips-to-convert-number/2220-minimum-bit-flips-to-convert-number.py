class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=0
        for i in str(bin(start^goal)[2:]):
            if i=='1':
                ans+=1
        return ans
        