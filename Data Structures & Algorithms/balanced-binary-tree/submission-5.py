# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Iterative DFS

        if not root:
            return True

        stack = [(root, False)]
        height = {None: 0}

        while stack:
            node, vis = stack.pop()
            
            if node:
                if vis:
                    left_h = height[node.left]
                    right_h = height[node.right]

                    diff = abs(left_h - right_h)

                    if diff > 1:
                        return False

                    height[node] = 1 + max(left_h, right_h)


                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return True
