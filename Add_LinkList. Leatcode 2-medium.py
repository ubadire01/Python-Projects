# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both lists until both are exhausted and there is no carry left.
        while l1 or l2 or carry:
            # Get the value from the current nodes of l1 and l2, or 0 if the node is None.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum of the current digits and the carry.
            total = val1 + val2 + carry
            
            # Update the carry for the next iteration.
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move the current pointer to the next node in the result list.
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
