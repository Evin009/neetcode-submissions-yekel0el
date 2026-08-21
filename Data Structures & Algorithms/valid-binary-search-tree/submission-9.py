# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #bst = left subtree < root < right subtree

        # check every node if its on right side the rnage - right < node < +inf
        # on left -inf < node < left

        if not root:
            return True

        def traverse(node, left_range, right_range) -> bool:
            if not node:
                return True
            
            if not (left_range < node.val < right_range):
                return False
            
            # both left and right side needs to be true
            return traverse(node.right, node.val, right_range) and traverse(node.left, left_range, node.val)

            
        
        return traverse(root, float('-inf'), float('inf'))

            

            
