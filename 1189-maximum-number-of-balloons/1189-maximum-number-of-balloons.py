class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balon=[0,0,0,0,0]
        for i in text:
            if i == 'b':
                balon[0]+=1
            elif i == 'a':
                balon[1]+=1
            elif i == 'l':
                balon[2]+=0.5
            elif i == 'o':
                balon[3]+=0.5
            elif i == 'n':
                balon[4]+=1
        return int(min(balon))
        