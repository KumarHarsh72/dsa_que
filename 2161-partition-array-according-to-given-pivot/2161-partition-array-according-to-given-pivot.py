class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        s=[]
        m=[]
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i==pivot:
                s.append(i)
            else:
                m.append(i)
        return l+s+m
        