# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # interative dfs
        if root is None:
            return None
        
        stack = [root]

        while stack:
            #gives the current node
            node = stack.pop()

            temp = node.left
            node.left = node.right
            node.right = temp


            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return root