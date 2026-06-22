class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        frnd=[]
        for i in order:
            if i in friends:
                frnd.append(i)
        return frnd
        