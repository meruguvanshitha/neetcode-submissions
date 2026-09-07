class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])  # Include nums[i]
            dfs(i + 1)
            
            subset.pop()            # Exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res