# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [[root, False]]
        height = {None: 0}
        # [1T, 2T, 4F,3T, 5T]
        max_dia = 0
        while stack:
            node, vis = stack.pop()

            if vis:
                left = height[node.left]
                right = height[node.right]

                dia = left + right
                max_dia = max(dia, max_dia)

                height[node] = 1 + max(left, right)

            else:
                stack.append([node, True])
                if node.right:
                    stack.append([node.right, False])
                if node.left:
                    stack.append([node.left, False])

        return max_dia

