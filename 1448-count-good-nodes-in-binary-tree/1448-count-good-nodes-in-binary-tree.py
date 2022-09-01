class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def pre(root,maax):
            nonlocal ans
            if not root: return 0
            
            if root.val>=maax:
                ans+=1
                # print(root.val)
            maax = max(root.val,maax)
            pre(root.left,maax)
            pre(root.right,maax)
        pre(root,float('-inf'))
        return ans
            