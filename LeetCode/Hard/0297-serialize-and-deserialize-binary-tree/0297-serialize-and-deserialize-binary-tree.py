# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.res = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        def traverse(root):
            if root is None:
                self.res.append('#')
                return
            self.res.append(str(root.val))
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return ' '.join(self.res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        treeList = data.split()
        self.p = -1
        def traverse(chars):
            if self.p == len(chars) - 1:
                return
            self.p += 1
            if chars[self.p] == '#':
                return None
            cur = TreeNode(int(chars[self.p]))
            cur.left = traverse(chars)
            cur.right = traverse(chars)
            return cur
        
        return traverse(treeList)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))