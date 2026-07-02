# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def travers(node):
            if node is None:
                return
            travers(node.left) # left traver
            ans.append(node.val) # add value in ans
            travers(node.right) # travers to right

        travers(root)
        return ans
        