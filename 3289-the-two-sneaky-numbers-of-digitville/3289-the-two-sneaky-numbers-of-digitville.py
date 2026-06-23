class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-2):
            nums.remove(i)
        return nums
        