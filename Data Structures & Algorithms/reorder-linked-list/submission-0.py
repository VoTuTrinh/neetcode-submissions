# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        l2 = self.reverse(l2)

        while l2:
            next_node1, next_node2 = l1.next, l2.next
            l1.next = l2
            l2.next = next_node1
            l1, l2 = next_node1, next_node2
    
    def reverse(self, linked_list: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, linked_list

        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

            

            
                
            


        

        