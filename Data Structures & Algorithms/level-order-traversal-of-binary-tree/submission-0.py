# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque


        if not root:
            return []

        res = []
        q = deque([root])  # 1. Start with the root node

        while q:
            level = []
            # 2. Process all nodes in the current row
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                # 3. Add kids to queue for the next row
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)  # 4. Save current row

        return res