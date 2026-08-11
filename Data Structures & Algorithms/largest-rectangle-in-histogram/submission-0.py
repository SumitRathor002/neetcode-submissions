class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                top_idx, top = stack.pop()
                res = max(res, top * (idx - top_idx))
                start = top_idx

            stack.append((start, h))
        
        for idx, h in stack:
            res = max(res, h * (len(heights) - idx))

        return res       
