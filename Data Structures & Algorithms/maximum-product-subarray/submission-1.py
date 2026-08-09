class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = 1
        res = max(nums)
        curr_min = 1
        curr_max = 2
        for n in nums:
            if n == 0:
                curr_min = 1
                curr_max = 1
            curr_max = max(curr_max*n, curr_min*n, n)
            curr_min = min(curr_max*n, curr_min*n, n)
            res = max(curr_max, res)

        return res