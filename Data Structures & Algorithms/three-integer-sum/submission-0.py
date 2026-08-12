class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums) - 1):
            items = set()
            for j in range(i + 1, len(nums)):
                if 0 - nums[i] - nums[j] in items:
                    res.add(tuple(sorted([nums[i], nums[j], 0 - nums[i] - nums[j]])))
                items.add(nums[j])
            
        return list(res)
