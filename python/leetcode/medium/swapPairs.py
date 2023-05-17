# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if the list is empty or has only one node, return the head
        if not head or not head.next:
            return head
        
        # initialize a dummy node to point to the head
        dummy = ListNode(-1)
        dummy.next = head
        
        # initialize pointers to keep track of current and next nodes
        prev = dummy
        curr = head
        
        while curr and curr.next:
            # store the next node in a variable
            nxt = curr.next
            
            # swap the current and next nodes
            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt
            
            # update the pointers to their new positions
            prev = curr
            curr = curr.next
        
        # return the new head
        return dummy.next
