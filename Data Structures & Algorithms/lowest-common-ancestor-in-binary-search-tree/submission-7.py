# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        # what type of tree? - BST
        # How to deal with curr node lgic when to move left or right? 
        # traversal stratergy: top-down or bottom up
        # base case 

        self.p = p
        self.q = q

        def traversal(root):
            cur = root

            while cur:
                # if either p and q less or greater than root
                if p.val < cur.val < q.val or q.val < cur.val < p.val:
                    return cur

                # if p or q val same as cur
                if p.val == cur.val or q.val == cur.val:
                    return cur

                # if p and q less than root - left subtree
                if p.val < cur.val and q.val < cur.val:
                    cur = cur.left
                # if p and q greater than root - right subtree
                if p.val > cur.val and q.val > cur.val:
                    cur = cur.right


        node = traversal(root)
        return node
