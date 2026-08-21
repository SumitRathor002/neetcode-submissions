class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_hours(k):
            hours = 0
            for p in piles:
                hours += p // k + bool(p % k)
            return hours

        l = 1
        r = max(piles)
        res = float('inf')
        while l < r:
            mid = (l + r) // 2
            hours = calc_hours(mid)
            if hours > h:
                l = mid + 1
            else:
                r = mid 
                res = min(res, mid)

        hours = calc_hours(l)
        if hours <= h:
            res = min(res, l)

        return res