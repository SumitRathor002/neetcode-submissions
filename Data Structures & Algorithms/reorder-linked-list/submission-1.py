# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 

        slow = head
        fast = head 
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next 

        second_half = slow.next

        node = second_half
        prev = None
        while node is not None:
            _next = node.next
            node.next = prev
            prev = node
            node = _next

        l2 = prev
        node = head
        while node is not None:
            _next = node.next
            node.next = l2
            node = l2
            l2 = _next

        



