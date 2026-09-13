class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(curr):
            if not curr: return None
            if curr in old_to_new: return old_to_new[curr]

            copy = Node(curr.val)
            old_to_new[curr] = copy

            for nxt in curr.neighbors:
                copy.neighbors.append(dfs(nxt))
            return copy

        return dfs(node)