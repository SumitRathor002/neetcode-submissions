class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0 
        r = len(nums)- 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # minimum must be to the right of mid
                l = mid + 1
            else:
                # mid could itself be the minimum
                r = mid

        return nums[l]
        # while l <= r:
        #     mid = (l + r ) // 2
        #     print(l, r, nums[mid])
        #     right = nums[mid+1] if (mid + 1) < len(nums) else float('inf')
        #     left = nums[mid - 1] if (mid - 1) >= 0 else float('inf')
        #     if left > nums[mid] and nums[mid] < right:
        #         res = nums[mid]
        #         break
            
        #     # left is already sorted search in right
        #     if nums[l] <= nums[mid]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
                
        # return min(res, nums[0])