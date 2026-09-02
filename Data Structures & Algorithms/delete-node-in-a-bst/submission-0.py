class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 1. Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2. Found it! Handle 0 or 1 child cases
            if not root.left: return root.right
            if not root.right: return root.left

            # 3. Handle 2 children case: find smallest on right, swap, and delete
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root