class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=[0]
        rs=[0]
        ans=[]
        for i in range(len(nums)-1):
            rs.append(rs[-1]+nums[i])
        for i in nums[::-1]:
            ls.append(ls[-1]+i)
        ls.pop()
        ls.reverse()
        for i in range(len(ls)):
            ans.append(abs(ls[i]-rs[i]))
        return ans


        