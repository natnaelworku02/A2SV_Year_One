# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        od = odd
        even = ListNode()
        ev = even
        ind = 0
        temp = head
        while temp:
            if ind %2 == 0:
                ev.next = temp
                ev = ev.next
            else:
                od.next = temp
                od = od.next
            temp = temp.next
            ind +=1
        ind -=1
        if ind %2==0:
            od.next = None
        else:
            ev.next = None
        ev.next = odd.next

        return even.next
