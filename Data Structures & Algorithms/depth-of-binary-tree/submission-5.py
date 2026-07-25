# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS

        '''
        - Use a stack to push visited nodes
        - to revert back we pop the node 

        - []
        res = 3
        '''

        # add depth as well when adding to stack
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            # if node is not null
            if node:
                res = max(res, depth) 
                stack.append([node.left, depth + 1]) #incerement the depth when adding at each level
                stack.append([node.right, depth + 1])


        return res

        

    
                
