class MyStack:

    def __init__(self):
        self.st = deque()
        

    def push(self, x: int) -> None:
        temp = deque()
        if self.st:
            while self.st:
                temp.append( self.st.popleft())
            self.st.append(x)
            while temp:
                self.st.append(temp.popleft())
        else:
            self.st.append(x)


        

    def pop(self) -> int:
        return self.st.popleft()
        

    def top(self) -> int:
        return self.st[0]
        

    def empty(self) -> bool:
        return len(self.st) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()