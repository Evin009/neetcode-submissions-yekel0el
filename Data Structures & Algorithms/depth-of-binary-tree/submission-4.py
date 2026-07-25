# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth - number of nodes along the longest path
        # depth = DFS

        '''
        APPROCH:
        - start from the root and check if root exist if yes first go to left side
        - recurisvely go to left side untill node is null
        - then          
        '''

        if not root:
            return 0
        
        #check left subtree
        left_depth = self.maxDepth(root.left)
        #check right subtree
        right_depth = self.maxDepth(root.right)

        #find the maximum depth and add the node itself
        return (max(left_depth, right_depth) + 1)        