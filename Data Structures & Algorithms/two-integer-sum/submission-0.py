class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, n in enumerate(nums):
            if target - n in seen:
                return [seen[target-n], idx]

            else:
                seen[n] = idx