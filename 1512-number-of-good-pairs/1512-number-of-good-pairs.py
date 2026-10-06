import math
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        good_pair=0
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for i in count:
            if count[i]>1:
                good_pair+=math.comb(count[i],2)
        return good_pair
        
        


        