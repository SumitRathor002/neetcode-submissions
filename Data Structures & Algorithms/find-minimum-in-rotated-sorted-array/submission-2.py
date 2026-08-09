class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (j + i)// 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]    
            else:
                if nums[mid] > nums[j]:
                    i = mid
                else:
                    j = mid
                      