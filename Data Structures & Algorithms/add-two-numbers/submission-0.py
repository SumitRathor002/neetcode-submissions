# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        while l1 is not None or l2 is not None:
            new_digit = getattr(l1, 'val', 0) + getattr(l2, 'val', 0) + carry
            carry = new_digit // 10
            new_digit = new_digit % 10
        
            if prev is None:
                prev = ListNode(new_digit, None)
                head = prev
            else:
                prev.next = ListNode(new_digit, None)
                prev = prev.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            prev.next = ListNode(carry, None)
            prev = prev.next

        return head


