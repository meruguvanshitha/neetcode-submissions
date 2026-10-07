class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        c1, c2 = Counter(s1), Counter(s2[:len(s1)])
        if c1 == c2: return True
        
        k = len(s1)
        for i in range(k, len(s2)):
            c2[s2[i]] += 1                      # Add new character entering window
            c2[s2[i - k]] -= 1                  # Remove old character leaving window
            if c2[s2[i - k]] == 0: 
                del c2[s2[i - k]]               # Cleanup zero counts for dict comparison
            
            if c1 == c2: return True
            
        return False