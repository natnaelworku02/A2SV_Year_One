# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy_cur = dummy
        dum = ListNode()
        dum.next = head
        temp = dum
        while temp and temp.next:
            if temp.next.val < x:
                dummy_cur.next = temp.next
                dummy_cur =  dummy_cur.next
                temp.next = temp.next.next
            else:
                temp = temp.next
        temp.next = None

        dummy_cur.next = dum.next
        return dummy.next

        