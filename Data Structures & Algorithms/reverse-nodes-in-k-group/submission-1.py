# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1
        
        passes = length // k
        res_head = None
        curr_head = head
        prev_head = None
        for _ in range(passes):
            rev = 0
            node = curr_head
            prev = None
            while rev < k:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                rev += 1
            
            if prev_head is not None:
                prev_head.next = prev
            
            prev_head = curr_head
            curr_head = temp
        
            if res_head is None:
                res_head = prev

        if length % k > 0:
            prev_head.next = curr_head


        if res_head is None:
            res_head = head

        return res_head
