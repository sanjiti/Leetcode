# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        output = ListNode()
        head_op = output
        while p1 and p2:
            if p1.val<p2.val:
                head_op.next = p1
                p1 = p1.next
            else:
                head_op.next = p2
                p2 = p2.next
            head_op = head_op.next
        
        head_op.next = p1 or p2
        return output.next