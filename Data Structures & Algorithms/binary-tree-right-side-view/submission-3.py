# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dfs at each depth we visit only onle on node - the right node
        # once we append that node of depth = len(res) move to next
        # we move to rigth side first if nothing on right then to left

        self.res = []

        def dfs(node, depth):
            if not node:
                return None
            
            # only append one element at each level - first element of right
            if len(self.res) == depth:
                self.res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return self.res
        

