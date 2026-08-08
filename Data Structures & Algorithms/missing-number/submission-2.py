class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        import functools 
        res = functools.reduce(
            lambda x,y : x^y, [*nums, *(i for i in range(len(nums)+1))]
            )
        return res
        