import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Step 1: Negate values to build a Max-Heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        # Step 2: Keep smashing until 0 or 1 stone remains
        while len(stones) > 1:
            first = heapq.heappop(stones)   # Heaviest stone (most negative)
            second = heapq.heappop(stones)  # Second heaviest stone
            
            if first != second:
                heapq.heappush(stones, first - second)
                
        # Step 3: Return the last stone (negated back) or 0 if empty
        return -stones[0] if stones else 0