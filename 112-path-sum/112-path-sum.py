# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, tar: int) -> bool:
        if not root: return False
        def fuc(node,suum):
            nonlocal tar
            if node:
                if suum+node.val == tar and not node.left and not node.right:
                    return True
                else:
                    return fuc(node.left,suum+node.val) or fuc(node.right,suum+node.val)
            else:
                return False
        return fuc(root,0)