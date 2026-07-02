# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def travers(node):
            if node is None:
                return
            travers(node.left) # left side travers
            travers(node.right) # right side travers
            ans.append(node.val) # add value

        travers(root) # calling function
        return ans
        