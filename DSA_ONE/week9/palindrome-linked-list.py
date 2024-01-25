# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = None
        cur = head
        while cur:
            if not temp:
                temp = ListNode(cur.val)
            else:
                node = ListNode(cur.val)
                node.next = temp
                temp = node
            cur = cur.next
        cur = head
        # print(temp)
        while cur and temp:
            if temp.val != cur.val:
                return False
            cur = cur.next
            temp = temp.next
        return True
