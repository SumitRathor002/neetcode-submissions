# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def remove(node, i = 1):
            length = None
            if node.next is None:
                length = i 
                print(length)
                
            
            if length is None:
                print(i, node.val)
                length = remove(node.next , i + 1)
            
            if i == length - n :
                node.next = node.next.next if node.next else None


            return length 
        
        length = remove(head)
        if length == n:
            return head.next if head.next else None

        return head
