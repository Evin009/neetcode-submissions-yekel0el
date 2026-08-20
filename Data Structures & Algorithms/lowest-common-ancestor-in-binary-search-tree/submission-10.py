# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # bst - left < root. < right
        # unique values 
        # descanants and ancestoers
        self.p = p
        self.q = q
        def traverse(node):
            if not node:
                return None
            
            if min(p.val, q.val) <= node.val <= max(q.val, p.val):
                return node
            
            if p.val < node.val and q.val < node.val:
                return traverse(node.left)
            if p.val > node.val and q.val > node.val:
                return traverse(node.right)
        
        return traverse(root)



    
        