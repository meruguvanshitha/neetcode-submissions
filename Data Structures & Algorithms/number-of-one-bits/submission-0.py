class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1  # Add 1 if the last bit is set
            n >>= 1         # Shift bits to the right
        return count