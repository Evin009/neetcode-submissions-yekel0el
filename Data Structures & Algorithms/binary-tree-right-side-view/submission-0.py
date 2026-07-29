# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # from right side view only one node is visible at each level
        # only need to append one rightmost element at each level

        if not root:
            return []

        queue = deque()
        queue.append(root)

        res = []

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # as we appending right to left only need to append the first element
                if i == 0:
                    res.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return res