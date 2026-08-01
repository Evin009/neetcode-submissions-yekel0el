# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder  - BST    
        # move to the left most element and start loking elements as they appear in ascending order if in BST

        if not root:
            return False
        
        self.prev = float("-inf")
        
        def valid(root):
            if not root:
                return True

            if not valid(root.left):
                return False
            
            if self.prev >= root.val:    
                return False
            self.prev = root.val

            return valid(root.right)

            
        
        return valid(root)
        
