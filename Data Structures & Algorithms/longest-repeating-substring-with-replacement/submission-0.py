class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # Expand the window by adding s[right]
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # If (window_length - max_freq) > k, window is invalid -> shrink from left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
        return len(s) - left