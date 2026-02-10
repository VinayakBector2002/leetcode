# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Order traversal -> lit the arr in order 
        result, stack, current = [], [], root
        while current or stack or len(result) < k:
            # go as far left as possible 
            while current:
                stack.append(current)
                current = current.left 
            # current is null now, i.e reached left most child 
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result[k - 1]
