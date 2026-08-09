class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return min(nums)

        i = 0
        j = len(nums) - 1
        while i <= j:
            
            mid = (j + i)// 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]    
            else:
                if nums[mid] > nums[j]:
                    i = mid
                else:
                    j = mid
                      