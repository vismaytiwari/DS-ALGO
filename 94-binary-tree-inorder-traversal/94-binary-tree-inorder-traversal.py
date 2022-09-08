class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        lst=[]
        self.pre(root,lst)
        return lst
    def pre(self,root,lst):
        if(root):
            self.pre(root.left,lst)
            lst.append(root.val)
            
            self.pre(root.right,lst)