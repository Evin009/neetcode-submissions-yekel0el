# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth_count = 0
        res = []

        if not root:
            return 0

        queue = collections.deque()

        queue.append(root)

        while queue:
            qLen = len(queue)
            level = []

            for i in range(qLen):
                node = queue.popleft()
                if node:
                    level.append(node)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return len(res)
            