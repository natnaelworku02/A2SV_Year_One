# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode(0)
        temp = node
        dummy = head
        dummy = dummy.next

        while dummy:
            if dummy.val:
                temp.val += dummy.val
            else:
                if dummy.next:
                    temp.next = ListNode()
                    temp = temp.next
            dummy = dummy.next

        return node 
