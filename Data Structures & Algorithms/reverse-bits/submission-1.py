class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n:
            bit = n & 1
            n = n >> 1
            res = res | bit << (31-i)
            i += 1
        return res        