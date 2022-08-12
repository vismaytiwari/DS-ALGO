class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def  check(r,p,q):
            if(r):    
                if(r.val>p.val and r.val>q.val):
                    return( check(r.left,p,q))
                if(r.val<p.val and r.val<q.val):
                    return(  check(r.right,p,q))
                return r
        return(check(root,p,q))
