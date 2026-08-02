# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # path - sequence of node connected with edge adjacent to each other
        # path sum - sum of values of node along the path 
        # only return the max path 
        # if any node value reduces the path sum don't include 
        # dfs bottom-up (postorder)

        self.max_path = float('-inf')

        def dfs(root):
            # base case
            if not root:
                return 0


            # left subtree max path sum
            # need to ignore if left or right child is neg
            left_sum = max(0,dfs(root.left))
            # right subtree max path sum
            right_sum = max(0,dfs(root.right))

            # calculating the current path 
            path = root.val + left_sum + right_sum
            # updating max path if it exists
            self.max_path = max(path, self.max_path)

            # returning the path with max sum 
            return root.val + max(left_sum, right_sum)
        
        dfs(root)
        return self.max_path