# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            #leaf node are assumed to be captured
            if not node: return 1
            l,r = dfs(node.left),dfs(node.right)
            if l==0 or r==0:
                ans+=1
                return 2
                
            elif l==2 or r==2:
                return 1
            
            else:
                return 0
        if dfs(root)==0: ans+=1
        return ans