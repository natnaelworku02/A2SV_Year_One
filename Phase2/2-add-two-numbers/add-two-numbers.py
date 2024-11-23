# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode()
        temp = ans
        carry = 0

        temp1 = l1
        temp2 = l2

        while temp1 or temp2:
            val = 0

            if temp1:
                # print(temp1.val,"1assd")
                val += temp1.val
            if temp2:
                val += temp2.val
                # print(temp2.val,"2wdf")
            
            val += carry
            # print(val)

            val = str(val)
            if len(val) >1:
                temp.val = int(val[-1])
                carry = int(val[0])
            else:
                temp.val = int(val)
                carry = 0
            
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
            
            if temp1 or temp2:
                temp.next = ListNode()
                temp = temp.next
        
        if carry:
            temp.next = ListNode(carry)
        
        return ans
