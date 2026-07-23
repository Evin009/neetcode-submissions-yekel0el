# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = length of the longest path between any two nodes
        # here we are taking length as number of edges/ connections between the nodes
         

        if not root:
            return 0 

        # find the lax length/ height of left subtree
        left_height = self.maxLength(root.left)

        # find the lax length/ height of right subtree
        right_height = self.maxLength(root.right)

        # adding left. + right heights to find diameter
        diameter = left_height + right_height

        # finding max dimater amoung all the nodes in the tree
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(sub, diameter)








    def maxLength(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxLength(root.left), self.maxLength(root.right))

        