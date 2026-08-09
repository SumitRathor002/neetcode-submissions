class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0
        for n in nums:
            if n-1 not in nums_set:
                i = n
                seq = 0
                while i in nums_set:
                    seq += 1
                    i += 1 
                
                max_seq = max(seq, max_seq)

        return max_seq