class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1

        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
            
        if len(t_map) != len(s_map):
            return False

        for k, v in t_map.items():
            if k not in s_map:
                return False
            if s_map[k] != v:
                return False
        
        return True

