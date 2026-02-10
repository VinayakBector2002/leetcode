'''
Input: Given the root of a binary tree
return: The maximum width of the given tree.

The maximum width of a tree 
    is the maximum width among all levels.

    The width of one level is defined 
        as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
        where the null nodes between the end-nodes that would be present in a complete 
        binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


Doubts:
    - Since root is optional what will be the width when root is null -> 0?

# Naïve 
    Reccursion O(2^d), max depth and then calculate 2^d 
# optimal 
    BFS O(number of nodes) -> level wise -> Keep track of maximum level and then 2^level 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        currMax = 0
        q = deque()

        def bfs():
            nonlocal currMax
            while q:
                # calculate current width 
                currMax = max(currMax, q[-1][1] - q[0][1] + 1) #edgecase of single element
                for i in range(len(q)):
                    curr, idx = q.popleft()
                    if curr.left:
                        q.append((curr.left, 2 * idx))
                    if curr.right:
                        q.append((curr.right, 2 * idx + 1))                    
        
        q.append((root,0))
        bfs()
        return currMax