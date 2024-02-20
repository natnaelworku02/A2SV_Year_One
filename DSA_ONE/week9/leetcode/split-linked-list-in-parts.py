# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        if head == None:
            for _ in range(k):
                ans.append(None)
            return ans
        size = 0
        temp = head
        while temp :
            size +=1
            temp = temp.next
        # dummy = ListNode(0,head)
        step = size // k
        mod = size % k
        if step < 1:
            cur, prev = head.next,head
            while cur:
                ans.append(prev)
                prev.next = None
                prev = cur
                cur = cur.next
            ans.append(prev)
            while len(ans) < k:
                ans.append(None)
        else:
            count = 0
            cur, prev = head.next,head
            move = step+1 if count < mod else step
            step_bool = False
            while prev:
                if move == step and not step_bool :

                    ans.append(prev)
                if move == step+1 :
                    ans.append(prev)
                    step_bool = True
                    # print("HI",prev.val)

                if move > 1:
                    cur = cur.next
                    prev = prev.next
                    move -=1
                    continue
                prev.next = None
                # print(prev.val, cur.val)
                prev = cur
                if cur:
                    cur = cur.next
                step_bool = False
                count +=1
                move = step+1 if count < mod else step
                # print(count,"_____",move,step)
        return ans
                
                

        