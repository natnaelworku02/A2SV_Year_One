class Node :
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        ind = 0
        cur_ptr = self.head
        while cur_ptr:
            if ind == index:
                return cur_ptr.val
            cur_ptr = cur_ptr.next
            ind +=1
        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node (val)
        else:
            node =Node(val)
            node.next = self.head
            self.head = node
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        ind = 0
        while temp and ind != index-1:
            temp = temp.next
            ind+=1
        if ind == index-1:
            node = Node(val)
            if temp != None:
                node.next = temp.next
                temp.next = node


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head =  self.head.next
            return
        temp = self.head
        ind = 0
        while temp and ind != index-1:
            temp = temp.next
            ind+=1
        if ind == index-1:
            if temp != None and temp.next != None:

                
            # print(temp.next.val)
                temp.next = temp.next.next
    
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)