# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        # temp = dummy

        def rev(temp):
            if temp and temp.next:
                nxt = temp.next
            else:
                return temp 

            temp.next = None
            while nxt and nxt.next:
                node = nxt.next
                nxt.next = temp
                temp = nxt 
                nxt = node
            nxt.next = temp
            # print (nxt)
            # print("_______")
            return nxt
        
        dummy = rev(dummy)
        temp = dummy
        prev = temp
        temp = temp.next
        cur_max = prev.val
        while prev and temp:
            if temp.val < cur_max:
                prev.next = temp.next
                temp = temp.next
            else:
                cur_max = max(cur_max,temp.val)
                prev = temp
                temp = temp.next
        
        head = rev(dummy)
        # print(dummy)
        return head


