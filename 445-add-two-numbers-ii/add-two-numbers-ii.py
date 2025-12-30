# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def createDeepStack(self, l1: Optional[ListNode]) -> List[ListNode]:
        stack = []
        current = l1
        while current:
            stack.append(current)
            current = current.next
        return stack
                
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack, l2_stack = self.createDeepStack(l1), self.createDeepStack(l2)
        last_node = None
        carry = 0
        while l1_stack or l2_stack:
            current_node = ListNode(val=carry, next=last_node)

            if l1_stack:
                l = l1_stack.pop()
                current_node.val += l.val

            if l2_stack:
                r = l2_stack.pop()
                current_node.val += r.val
            
            carry = current_node.val // 10
            current_node.val = current_node.val % 10
            last_node = current_node
        
        if carry:
            last_node = ListNode(val=carry, next=last_node)
        
        return last_node



        