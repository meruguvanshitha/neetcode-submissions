class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path)
                return

            for i in range(start, len(nums)):
                if nums[i] <= remaining:
                    backtrack(i, path + [nums[i]], remaining - nums[i])

        backtrack(0, [], target)
        return res