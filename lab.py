"""Definition for singly-linked list. """
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode)-> ListNode:
        """reference to the head c """
        curr = head 
        prev = None
        """curr is node(2) """
        while curr is not None:  
            print(f'current value:: {curr.val}')
            print(f'next value: {curr.next.val}')
            print(f'previous value: {prev}')
            """ storing curr.next in a temporary variable"""
            nextTemp = curr.next  
            """curr.next ^^ is Node(3) and we store node(3) in nextTemp"""
            """assigning next to previous node | we assign cur.next to node(1) """
            curr.next = prev 
            print('reassigning previous')
            prev = curr
            curr = nextTemp
        return prev

head = [1,2,3,4,5]

