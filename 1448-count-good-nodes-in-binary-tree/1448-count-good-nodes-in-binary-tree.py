class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        def test(node, lower):
            if not node:
                return
            if node.val >= lower:
                self.count += 1
                lower = node.val
            
            test(node.left, lower)
            test(node.right, lower)
            
        test(root, float("-inf"))
        return self.count