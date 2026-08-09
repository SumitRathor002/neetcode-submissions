class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)

        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (j + i)// 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] >= nums[i]:
                i = mid + 1
            else:
                j = mid  
                      