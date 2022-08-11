# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seet = set()
        def create(node,v ):
            if not node : return None
            node.val = v
            self.seet.add(node.val)
            create(node.left,2*node.val+1) 
            create(node.right,2*node.val+2)
        create(root,0)
            

    def find(self, target: int) -> bool:
        if target in self.seet: return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)