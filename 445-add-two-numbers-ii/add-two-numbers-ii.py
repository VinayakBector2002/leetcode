# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseDeep(self, l1: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = l1
        while current:
            temp = current.next
            current.next = prev
            prev,current = current, temp
        return prev 
                
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = self.reverseDeep(l1), self.reverseDeep(l2)
        last_node = None
        carry = 0
        while l1 or l2:
            current_node = ListNode(val=carry, next=last_node)

            if l1:
                current_node.val += l1.val
                l1 = l1.next

            if l2:
                current_node.val += l2.val
                l2 = l2.next
            
            carry = current_node.val // 10
            current_node.val = current_node.val % 10
            last_node = current_node
        
        if carry:
            last_node = ListNode(val=carry, next=last_node)
        
        return last_node



        