# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        node = dummy
        # temp = head
        ind = 0
        while temp and temp.next:
            if ind >=n :
                node = node.next
            temp = temp.next
            ind +=1
        # print(node)
        node.next = node.next.next
        # print(node)
        return dummy.next

            
