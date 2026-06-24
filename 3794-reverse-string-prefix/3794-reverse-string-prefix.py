class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        m=s[0:k]
        return m[::-1]+s.replace(m,"",1)
        