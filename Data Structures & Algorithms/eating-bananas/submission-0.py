class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l = 1
        r = max(piles)
        result = max(piles)

        while l <= r:
            mid = (l + r) // 2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / mid)

            if total > h:
                l = mid + 1
                
            else:
                r = mid - 1
                if mid < result:
                    result = mid
        
        return result

                
            
            

            


