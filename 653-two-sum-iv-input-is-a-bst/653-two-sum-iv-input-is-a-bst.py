class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dic = {}
        def traversal(node):
            if not node: return False
            if node.val in dic.keys():
                return True
            else:
                dic[k-node.val] = node.val

            return traversal(node.left) or traversal(node.right)
        
        return traversal(root)