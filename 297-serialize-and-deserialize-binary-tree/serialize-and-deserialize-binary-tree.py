# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""     
            
        answer = []

        def bfs(node):
            q = deque([node])
            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr == None:
                        answer.append("None")
                        continue

                    q.append(curr.left if curr.left else None)
                    q.append(curr.right if curr.right else None)
                    
                    answer.append(str(curr.val))
                    
        bfs(root)
        return ",".join(answer)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "":
            return []

        cast = data.split(",")
        root = TreeNode(cast[0])
        q = deque([root])
        n = len(cast)
        i = 1  
        
        while q:
            current = q.popleft()

            if i < n and cast[i] != 'None':
                current.left = TreeNode(cast[i])
                q.append(current.left)
            i += 1
            
            if i < n and cast[i] != 'None':
                current.right = TreeNode(cast[i])
                q.append(current.right)
            i += 1 
        
        return root

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))