# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:    


        self.count = 0 
        
        def traverse(node, max_val):
                if not node:
                    return None
                
                if node.val >= max_val:
                    self.count += 1
                    max_val = max(node.val, max_val)

                traverse(node.left, max_val)
                traverse(node.right, max_val)
            
        traverse(root, float('-inf'))
        return self.count

        # max_val = float('-inf')
        # traverse(root,max_val)
        # return self.count

 
            

