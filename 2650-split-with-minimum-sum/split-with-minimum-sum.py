class Solution:
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))
        s =''.join(s)
        n = len(s)
        ls = s[:n:2]
        rs = s[1:n:2]
        return int(ls) + int(rs)
        