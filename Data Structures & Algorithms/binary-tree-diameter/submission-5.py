# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # iterative dfs

        '''
        - To calcaute the diameter we need the length of right and left first - so Postorder traversal
        '''
        if not root:
            return 0

        stack = [(root, False)]
        height = {None: 0}
        max_dia = 0

        while stack:
            node, vis = stack.pop()
            if node:
                if vis:
                    # first time when reach at the last child node its left and right are None so it works
                    left_h = height[node.left]
                    right_h = height[node.right]

                    dia = left_h + right_h
                    max_dia = max(max_dia, dia)

                    # store the height of the child nodes from bottom onwards to up
                    height[node] = 1 + max(left_h, right_h)

                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return max_dia