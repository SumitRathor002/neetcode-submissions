class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        stack_idx = -1
        
        for idx, t in enumerate(temperatures): 
            while stack and stack[-1][1] < t:
                p_idx, p_temp = stack.pop()
                res[p_idx] = idx - p_idx

            stack.append((idx, t)) 

        return res