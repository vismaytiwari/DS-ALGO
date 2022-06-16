# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        val=[]
        def ser(node):
            if node:
                val.append(str(node.val))
                ser(node.left)
                ser(node.right)
            else:
                val.append("$")
        ser(root)
        return " ".join(val)

    def deserialize(self, data):
        print(data)
        def doit():
            val = next(vals)
            if val == '$':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        
        vals = iter(data.split())
        return doit()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))