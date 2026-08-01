# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, left, right) -> bool:
            if not root:
                return True
            
            if not (left < root.val < right):
                return False
            
            left_side = valid(root.left, left, root.val) # returns true
            right_side = valid(root.right, root.val, right) # 

            return left_side and right_side

        return valid(root, float("-inf"), float("inf"))