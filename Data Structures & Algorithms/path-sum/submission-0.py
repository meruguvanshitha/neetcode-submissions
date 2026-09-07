# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
       
        if not root:
            return False

        # If it's a leaf node, check if current node's value matches targetSum
        if not root.left and not root.right:
            return targetSum == root.val

        # Recurse on left and right subtrees with updated targetSum
        remaining_sum = targetSum - root.val
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))