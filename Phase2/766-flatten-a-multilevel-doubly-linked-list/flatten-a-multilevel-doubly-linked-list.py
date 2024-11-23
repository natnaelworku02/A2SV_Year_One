"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        temp = head

        while temp and temp.next:
            temp = temp.next
        

        def link(nxt,node):

            temp = node.child

            while temp and temp.next:
                temp = temp.next
            
            if nxt:
                temp.next = nxt
                nxt.prev = temp

            while temp :
                if temp.child:
                    link(temp.next,temp)
                if temp.prev:
                  temp = temp.prev
                else:
                    break

            # if temp.child:
                # link(temp.)
            node.next = temp
            temp.prev = node

            node.child = None


        while temp :
            if temp.child:
                link(temp.next,temp)
            if temp.prev:
                temp = temp.prev
            else:
                break

        # print(temp.val)
        # if temp.child:
        #     link(temp.next,temp)
        # t = head
        # while t:
        #     print(t.val,end=" ")
        #     t = t.next
        # print()
        return head

            

            

        