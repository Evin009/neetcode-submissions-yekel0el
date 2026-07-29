# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal
        # use queue
        # all the elements of a particuar level only remains in the queue rest not present

        queue = deque()

        if not root:
            return []
        
        cur = root
        queue.append(cur)
        res = []

        while queue:

            node_lis = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node_lis.append(node.val)
            
            res.append(node_lis)
        return res




