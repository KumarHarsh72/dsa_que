class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d=date.split("-")
        for i in range(len(d)):
            d[i] = str(bin(int(d[i]))[2:])
        return "-".join(d)
        