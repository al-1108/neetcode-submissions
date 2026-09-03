class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            hours = 0
            eat_rate = l + (r-l) // 2
            for bananas in piles:
                hours += (bananas+eat_rate-1) // eat_rate
            if hours > h:
                l = eat_rate + 1
            else:
                r = eat_rate-1
        return l


        