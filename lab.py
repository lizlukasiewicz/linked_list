# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode)-> ListNode:
        curr = head # reference to the head c
        prev = None
        while curr is not None: # curr is node(2)
            print(f'current value:: {curr.val}')
            print(f'next value: {curr.next.val}')
            print(f'previous value: {prev}')
            nextTemp = curr.next # storing curr.next in a temporary variable 
            #curr.next is Node(3) and we store node(3) in nextTemp
            curr.next = prev #assigning next to previous node | we assign cur.next to node(1)
            print('reassigning previous')
            prev = curr
            curr = nextTemp
        return prev

head = [1,2,3,4,5]