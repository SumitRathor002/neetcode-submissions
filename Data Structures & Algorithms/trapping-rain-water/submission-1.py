class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0]
        maxL = height[0]
        maxR = height[-1]
        for h in height[1:]:
            maxL = max(maxL, h)
            max_left.append(maxL)

        for r in range(len(height) - 2, -1, -1 ):
            maxR = max(maxR, height[r])
            max_right.append(maxR)

        max_right = max_right[::-1]

        trapped = 0
        for idx, h in enumerate(height):
            trapped += max(min(max_left[idx], max_right[idx]) - h, 0)
        
        return trapped