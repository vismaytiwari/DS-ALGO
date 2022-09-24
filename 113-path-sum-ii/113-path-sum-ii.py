class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def pre(node,val,path):
            nonlocal targetSum
            if node:
                val = val+node.val
                path.append(node.val)
                if node.left is None and node.right is None :
                    if val==targetSum: ans.append(path.copy())
                   
                else:
                    if node.left: pre(node.left,val,path)
                    if node.right: pre(node.right,val,path)
                path.pop()    
        pre(root,0,[])
        return ans