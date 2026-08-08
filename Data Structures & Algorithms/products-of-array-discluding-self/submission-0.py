class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        
        for n in nums[:-1]:
            prefix.append(n * prefix[-1])

        for r_idx in range(len(nums)-1, 0, -1 ):
            postfix.append(nums[r_idx] * postfix[-1])

        return [ prefix[i] * postfix[len(postfix)-1-i]  for i in range(len(prefix))]
