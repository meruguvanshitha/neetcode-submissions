
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Keep only the k largest elements in the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        
        # Maintain heap size of k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The smallest element in a min-heap of size k is the kth largest overall
        return self.min_heap[0]