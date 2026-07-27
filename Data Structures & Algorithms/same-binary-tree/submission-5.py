# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # equivalent = same structure and same value nodes
        
        # both are null return T
        if not p and not q:
            return True 

        # only one of them is null return F
        if not p or not q:
            return False

        # values are not same
        if p.val != q.val:
            return False
        
        
        left_subtree = self.isSameTree(p.left, q.left)
        right_subtree = self.isSameTree(p.right, q.right)

        # return both val true
        return left_subtree and right_subtree
        