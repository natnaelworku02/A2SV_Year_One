# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ans = None

        while cur:
            newNode = ListNode(cur.val)
            if not ans:
                ans = newNode
            else:
                temp = ans
                newNode.next=ans
                ans = newNode
                
            cur = cur.next
        return ans