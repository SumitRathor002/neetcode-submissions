# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
        
    #     lists = sorted(lists, key = lambda x: x.val if x else float('inf'))
    #     head = lists[0]
    #     node = head
    #     if lists[0]:
    #         lists[0] = lists[0].next
        
    #     while any(lists):
    #         lists = sorted(lists, key = lambda x: x.val if x else float('inf'))
    #         node.next = lists[0]
    #         node = node.next

    #         if lists[0]:
    #             lists[0] = lists[0].next
            
    #     return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeLists(l1, l2):
            if l1 is None:
                return l2
            
            if l2 is None:
                return l1

            if l1.val < l2.val:
                head = l1 
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
            
            node = head
            while l1 is not None or l2 is not None:
                if l2 is None or (l1 is not None and l1.val < l2.val):
                    node.next = l1
                    l1 = l1.next 
                else:
                    node.next = l2
                    l2 = l2.next 
                
                node = node.next

            return head

        merged_lists = lists 
        while len(merged_lists) > 1:
            temp = []
            for i in range(0, len(merged_lists), 2):
                l1 = merged_lists[i]
                l2 = merged_lists[i + 1] if (i+1) < len(merged_lists) else None
                merged = mergeLists(l1, l2)
                temp.append(merged)
            

            merged_lists = temp

        return merged_lists[0]