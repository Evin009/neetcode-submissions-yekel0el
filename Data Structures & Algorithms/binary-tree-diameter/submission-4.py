# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDia = 0


        # returns height
        def dfs(root):
            # base case to break recurision
            if not root:
                return 0 

            # recursive cases

            # traverse left subtree
            left_subtree_length = dfs(root.left)

            # traverse right subtree
            right_subtree_length = dfs(root.right)

            # adding left and right height for diameter
            dia = left_subtree_length + right_subtree_length
            #updating maxDia
            self.maxDia = max(self.maxDia, dia)

            # adding the max height by adding the connnection of max length of children to node
            return 1 + max(left_subtree_length, right_subtree_length)

        dfs(root)
        return self.maxDia
        
