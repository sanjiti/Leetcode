# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxval):
            if root is None:
                return 0
            count = 1 if root.val>=maxval else 0
            maxval = max(maxval, root.val)
            
            count += helper(root.left, maxval)
            count += helper(root.right,maxval)
            return count
        return helper(root,root.val )