class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the position of valid elements
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move the valid element to the front
                k += 1             # Increment our pointer
                
        return k  # k represents the count of elements not equal to val