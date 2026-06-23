class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        have=0
        for i in stones:
            if i in jewels:
                have+=1
        return have
        