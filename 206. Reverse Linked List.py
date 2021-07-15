# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #using iterative method
        curr = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head
        
        #using recursive method
        '''p = head
        if p.next == None:
            head = p
            return
        self. reverseList(p)
        q = p.next
        q.next = p
        p.next = None '''
        