# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def oddEvenList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         start = head
#         end = head
#         count =0
        
    
#         while end and end.next:
#             end = end.next
#             count = count+1
            
        
#         if count&1:
#             counter = (count/2) +1
#         else:
#             counter = count/2
            
#         while counter:
#             end.next = start.next
#             start.next = end.next.next
#             end.next.next = None 
#             start = start.next
#             end = end.next
#             counter = counter -1
            
#         return head
    
        
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head is None):
            return head
        odd = head
        even = head.next
        evenhead = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = evenhead
        
        return head
    
        
        
    
        
        
        
        
        
        
        
        
    
        
        
        
        
        