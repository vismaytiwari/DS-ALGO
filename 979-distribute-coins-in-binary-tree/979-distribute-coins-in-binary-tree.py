# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node: return 0
            l,r=dfs(node.left),dfs(node.right)
            #check for left and right
            #our ans is total number of coins they have, we will not consider whether a node has one or more or even less then one.
            ans += abs(l)+abs(r)
            #at any point number of moves will be euqual to total coins of sub tree + itself and -1 because it need to have atleast one coin
            return l+r+node.val-1
        dfs(root)
        return ans