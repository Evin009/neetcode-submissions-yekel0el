# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = length of the longest path edges between two nodes
        # diameter = max length right + max length left
        # DFS Recusrive

        '''
        - we start by measing the left and right sides length 
        - calucate the max length at each node
        - add the max length of left and right sides to get diamter 
        - repeat the process of all the nodes in the tree 
        - finally return the max length/ diameter
        '''

        if not root:
            return 0

        left_side = self.maxHeight(root.left)
        right_side = self.maxHeight(root.right)         

        diameter = left_side + right_side

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)) 

        return max(sub, diameter)
    
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_subtree = self.maxHeight(root.left)
        right_subtree = self.maxHeight(root.right)

        return max(left_subtree, right_subtree) + 1

