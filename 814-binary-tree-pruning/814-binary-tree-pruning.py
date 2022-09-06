class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def f(r):
            if(r):
                r.left=f(r.left)
                r.right=f(r.right)
                if(r.val==0 and r.left==None and r.right==None):
                    return None
                return r
            return None
        f(root)
        if(root and root.val==0 and root.left==None and root.right==None):
            return None
        return root