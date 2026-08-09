class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = 1
        min_ = 1
        for n in nums:
            max_ = max(max_*n, min_*n, n)
            min_ = min(max_*n, min_*n, n)

        return max_