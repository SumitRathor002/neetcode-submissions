"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        import copy
        node = head
        nodes = {}
        ref = id(node)
        head2 = copy.copy(node)
        nodes[ref] = head2
        next_ref = id(node.next)
        random_ref = id(node.random)

        if next_ref not in nodes:
            head2.next = copy.copy(node.next)
            nodes[next_ref] = head2.next
        else:
            head2.next = nodes[next_ref]

        if random_ref not in nodes:
            head2.random = copy.copy(node.random) 
            nodes[random_ref] = head2.random
        else:
            head2.random = nodes[random_ref]

        node = node.next
        while node is not None:
            ref = id(node)
            if ref not in nodes:
                node2 = copy.copy(node)
                nodes[ref] = node2
            else:
                node2 = nodes[ref]

            next_ref = id(node.next)
            random_ref = id(node.random)
            
            if next_ref not in nodes:
                node2_next = copy.copy(node.next) 
                nodes[next_ref] = node2_next
            else:
                node2_next = nodes[next_ref]
            
            if random_ref not in nodes:
                node2_random = copy.copy(node.random)
                nodes[random_ref] = node2_random
            else:
                node2_random = nodes[random_ref]

            node2.next = node2_next 
            node2.random = node2_random

            node = node.next

        return head2
            

            