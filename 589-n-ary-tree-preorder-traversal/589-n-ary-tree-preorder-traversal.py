class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        preorder_list = []
        
        def dfs(root):
            
            if not root: return
            
            preorder_list.append(root.val)
            for child in root.children:
                dfs(child)
                
        dfs(root)
        
        return preorder_list