"""
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the 
first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # traverse list 1
        
        # traverse list 2
        
        #at each step, compare the values at each node
        
        #put the lower value in the new list
        
        #traverse through that list
        new_node = ListNode() # new empty node to build a new list
        temp = new_node # temp = temp.next
        while l1 and l2: #while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1  #adds l1 to the new list were building
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next #adds the l1 or l2 to the end of the list
        if l1 is not None:  #if l1 is not empty,
            temp.next = l1 # add l1 to the end
        else: # implies that l2 is not None
            temp.next = l2
        
        return new_node.next  # return new_node is the new list that has a 0 value in there
                            # new_node.next starts at the 1 

"""
RECURSIVELY::
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode)-> ListNode:
        if not l1 and not l2: return None
        elif not l1 or (l2 and l1.val > l2.val):
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
"""