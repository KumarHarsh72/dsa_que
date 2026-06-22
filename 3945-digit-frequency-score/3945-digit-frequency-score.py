class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq=[0,0,0,0,0,0,0,0,0,0] #this will store the frequesncy of 0 to 9
        for i in str(n):
            freq[int(i)] += 1
        print(freq)
        score=0
        for i in range(10):
            score += i*freq[i]
        print(score)
        return score
        