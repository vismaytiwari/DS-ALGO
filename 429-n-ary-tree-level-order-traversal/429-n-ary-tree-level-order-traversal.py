"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q=[root]
        ans = []
        while q!=[]:
            temp2 = [ ]
            for x in q:
                if x : temp2.append(x.val)
            if temp2:
                ans.append(temp2)
            temp = []
            for node in q :
                if node: temp.extend(node.children)
            q = temp
            
        return ans