# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        UNDERSTAND:
        - max path sum
        - path? seq of nodes where each pair of adj nodes has an edge connecting
        - node cannot appear more than once
        - output: max sum in a any path

        Constarinst: can be neg, duplicate, zero 
        regarndless we need max sum 

        - need to use dfs as path problem 
        - traverse left and right find sum and add them and store to look make
        - go to next node
        '''

        self.max_path_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))

            path_sum = left + right + node.val

            self.max_path_sum = max(self.max_path_sum, path_sum)

            return node.val + max(left, right)
        
        dfs(root)
        return self.max_path_sum

            
            

        
            












