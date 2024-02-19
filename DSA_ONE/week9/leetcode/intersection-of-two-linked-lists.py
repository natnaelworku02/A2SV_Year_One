# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        di = set()
        temp = headA
        while temp:
            di.add(temp)
            temp = temp.next
        temp = headB
        # print(di)
        while temp:
            if temp in di:
                return temp
            temp = temp.next
        return None
        