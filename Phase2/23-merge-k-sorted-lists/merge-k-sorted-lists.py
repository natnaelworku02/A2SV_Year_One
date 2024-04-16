# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for i in range(len(lists)):
            node = lists[i]
            while node:

                nums.append(node.val)
                node = node.next
        
        heapq.heapify(nums)
        # print(nums)
        # return
        ans = ListNode(heapq.heappop(nums)) if nums else None
        temp = ans

        for i in range(len(nums)):
            temp.next = ListNode(heapq.heappop(nums))
            temp = temp.next
            # temp = ans.next
        
        return ans
