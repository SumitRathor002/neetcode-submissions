class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def get_count_map(s):
        #     res = {}

        #     for char in s:
        #         if char in res:
        #             res[char] += 1
        #         else:
        #             res[char] = 1

        #     return res

        # def is_anagram(s1, s2):
        #     if len(s1) != len(s2):
        #         return False
            
        #     s1_map = get_count_map(s1)
        #     s2_map = get_count_map(s2)

        #     return s1_map == s2_map

        def get_count_array(s):
            map = [0 for i in range(26)]
            for char in s:
                map[ord(char) - 97] += 1

            return tuple(map)

        res = {}
        for s in strs:
            count_map = get_count_array(s)
            if count_map in res:
                res[count_map].append(s)
            else:
                res[count_map] = [s] 

        return list(res.values())


