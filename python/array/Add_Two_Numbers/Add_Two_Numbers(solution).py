# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # Dummy head for result list
        current = dummy
        carry = 0

        # Traverse both lists until both are exhausted
        while l1 or l2 or carry:
            # Extract values (0 if node doesn't exist)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            # Create new node for current digit
            current.next = ListNode(new_val)
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        
