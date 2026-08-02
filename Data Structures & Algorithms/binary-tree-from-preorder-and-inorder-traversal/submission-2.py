# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # creating a hashmap to store inorder array and easy lookup of index vals0
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        

        def helper(pre_left, pre_right, in_left, in_right):
            if in_left > in_right:
                return None

            root = TreeNode(preorder[pre_left])
            mid = inorder_map[preorder[pre_left]]

            left_side = mid - in_left
            root.left = helper(pre_left + 1, pre_left + left_side, in_left, mid - 1)
            root.right = helper(pre_left + left_side + 1, pre_right, mid + 1, in_right)

            return root
        
        return helper(0, len(preorder)-1, 0, len(inorder)-1)
        