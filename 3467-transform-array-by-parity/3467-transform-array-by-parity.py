class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[0]%2==0:
                nums.append(0)
            else:
                nums.append(1)
            nums.pop(0)
        nums.sort()
        return nums
        