class Solution:
    hmap = {0:0, 1:1,2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.hmap:
            return self.hmap[n]
        else:
            res = self.climbStairs(n-2) + self.climbStairs(n-1)
            self.hmap[n] = res
            return res