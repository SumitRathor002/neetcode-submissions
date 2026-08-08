class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        res = 0 
        while n:
            n = n & (n-1)
            res += 1
        return res

    def countBits(self, n):
        dp = [0]
        for i in range(1, n+1):
            dp.append(Solution.hammingWeight(i))
        
        return dp