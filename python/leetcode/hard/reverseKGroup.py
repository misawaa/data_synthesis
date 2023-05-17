# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # if the list is empty or has only one node, return the head
        if not head or not head.next or k == 1:
            return head
        
        # initialize a dummy node to point to the head
        dummy = ListNode(-1)
        dummy.next = head
        
        # initialize pointers to keep track of current and previous nodes
        prev = dummy
        curr = head
        
        while curr:
            # count the number of nodes in the current group
            count = 0
            temp = curr
            while temp and count < k:
                temp = temp.next
                count += 1
            
            # if the current group has k nodes, reverse the group
            if count == k:
                # reverse the current group of nodes
                for i in range(k-1):
                    nxt = curr.next
                    curr.next = nxt.next
                    nxt.next = prev.next
                    prev.next = nxt
                
                # update the pointers to their new positions
                prev = curr
                curr = curr.next
            else:
                break
        
        # return the new head
        return dummy.next
