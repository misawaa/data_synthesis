# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # handle base cases
        if not head or not head.next or k == 0:
            return head
        
        # compute the length of the linked list and the last node
        length, last = 1, head
        while last.next:
            length += 1
            last = last.next
        
        # compute the actual value of k
        k %= length
        
        # handle the case where k is zero
        if k == 0:
            return head
        
        # find the new tail and the new head
        new_tail = head
        for i in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # rotate the linked list
        new_tail.next = None
        last.next = head
        
        return new_head
