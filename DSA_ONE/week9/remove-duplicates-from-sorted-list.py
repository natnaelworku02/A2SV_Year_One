# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-200)
        dummy.next = head
        temp  = dummy
        di = {}
        while temp and temp.next:
            if temp.next.val in di:
                temp.next = temp.next.next
            else:
                di[temp.next.val] = 1
                temp = temp.next
        dummy.next = None
        return head
