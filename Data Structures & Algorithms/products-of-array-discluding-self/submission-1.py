class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for n in nums[:-1]:
            res.append(n * res[-1])

        postfix = nums[-1]

        for r_idx in range(len(nums) - 2, -1, -1):
            res[r_idx] = res[r_idx] * postfix
            postfix = postfix * nums[r_idx] 


        return res