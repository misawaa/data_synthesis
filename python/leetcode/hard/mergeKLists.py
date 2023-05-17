# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Remove empty lists from the input
        lists = [lst for lst in lists if lst]
        
        # Initialize the min-heap with the first element of each list
        heap = [(lst.val, i, lst) for i, lst in enumerate(lists)]
        heapq.heapify(heap)
        
        # Initialize the result list
        dummy = ListNode(0)
        tail = dummy
        
        # Continue until the heap is empty
        while heap:
            # Extract the minimum element from the heap
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            
            # If the list still has elements, add the next element to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
