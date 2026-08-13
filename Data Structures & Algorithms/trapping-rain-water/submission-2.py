class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        l = 0
        r = len(height) - 1
        trapped = 0
        maxL, maxR = height[0], height[-1] 
        while l < r:
            if maxL < maxR:
                l += 1
                trapped += max(maxL - height[l], 0 )
                maxL = max(maxL, height[l])
            else:
                r -= 1
                trapped += max( maxR - height[r], 0 )
                maxR = max(maxR, height[r])


        return trapped