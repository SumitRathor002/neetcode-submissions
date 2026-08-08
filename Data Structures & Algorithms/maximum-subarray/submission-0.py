class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = float('-inf')
        curr_sum = float('-inf')
        for n in nums:
            if curr_sum + n < n:
                curr_sum = n 
            else:
                curr_sum = curr_sum + n

            max_ = max(max_ , curr_sum)

        return max_