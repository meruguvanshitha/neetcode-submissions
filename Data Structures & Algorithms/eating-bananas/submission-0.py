class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed 'mid'
            hours = sum(math.ceil(pile / mid) for pile in piles)
            
            if hours <= h:
                right = mid      # Speed works, try to find a smaller speed
            else:
                left = mid + 1   # Too slow, need a faster speed
                
        return left