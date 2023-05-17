# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If one of the lists is empty, return the other one
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # Create a dummy node to start building the merged list
        dummy = ListNode(0)
        # Pointer to keep track of the current node of the merged list
        curr = dummy
        
        # Traverse both lists at the same time
        while list1 and list2:
            # Compare the values of the nodes from list1 and list2
            if list1.val <= list2.val:
                # Append the smaller node to the merged list
                curr.next = list1
                # Move the pointer to the next node of list1
                list1 = list1.next
            else:
                # Append the smaller node to the merged list
                curr.next = list2
                # Move the pointer to the next node of list2
                list2 = list2.next
            # Move the pointer of the merged list to the newly appended node
            curr = curr.next
        
        # Append the remaining nodes of the non-empty list to the merged list
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        # Return the head of the merged list (excluding the dummy node)
        return dummy.next
