# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        if head is None or head.next is None:
            return False
        
        while slow is not None and fast is not None:
            slow = slow.next 
            fast = fast.next.next if fast.next else fast.next
            if slow is fast:
                return True

        return False
        