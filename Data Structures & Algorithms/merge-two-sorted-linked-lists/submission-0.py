# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        ptr = None
        head = None
        
        if not list1 and not list2:
            return head

        if list2 and ((not list1) or list2.val < list1.val) :
            head = list2
            ptr2 = ptr2.next
        else:
            head = list1
            ptr1 = ptr1.next

        ptr = head
        
        while ptr1 is not None or ptr2 is not None:
            if ptr1 is None:
                print(None)
                ptr.next = ptr2
                return head
                
            if ptr2 is None:
                ptr.next = ptr1
                return head

            if ptr1.val < ptr2.val:
                ptr.next = ptr1
                ptr = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr = ptr2
                ptr2 = ptr2.next

            print(ptr.val, getattr(ptr1, 'val', None),  getattr(ptr2, 'val', None))

        return head

