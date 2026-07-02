# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root is None:
            return ans
        que = deque([root])
        while que:
            level=[]
            sze = len(que)
            for _ in range(sze):
                node  = que.popleft()
                level.append(node.val)
                if(node.left):
                    que.append(node.left)
                if(node.right):
                    que.append(node.right)
                # now add in level in ans
            ans.append(level)
        return ans
