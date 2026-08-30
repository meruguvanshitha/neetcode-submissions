# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        res = []
        
        for i in range(len(pairs)):
            while i > 0 and pairs[i - 1].key > pairs[i].key:
                pairs[i], pairs[i - 1] = pairs[i - 1], pairs[i]
                i -= 1
            
            res.append(pairs.copy())
            
        return res