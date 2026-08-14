# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node is not None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        # print(prev.val if prev else None, node.val, node.next.val if node.next else None, temp.val)
        return prev