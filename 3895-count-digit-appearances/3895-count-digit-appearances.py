class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans=0
        for i in nums:
            while i!=0:
                if i%10==digit:
                    ans+=1
                i=i//10
        return ans
        