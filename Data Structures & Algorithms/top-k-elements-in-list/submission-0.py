class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [set() for _ in range(len(nums))]     
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq[freq_map[n] - 1].remove(n)
                freq_map[n] += 1 
                freq[freq_map[n] -1].add(n)
            else:
                freq_map[n] = 1
                freq[0].add(n)
        
        n = len(freq) - 1
        res = []
        while len(res) < k and n >= 0:
            res.extend(freq[n])
            n -= 1
        
        return res