class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       return any(Counter(s1)==Counter(s2[i:i+len(s1)]) for i in range(len(s2) - len(s1)+1))