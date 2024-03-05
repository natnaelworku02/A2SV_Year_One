class  NodeList:
    def __init__ (self,link,next = None,prev = None):
        self.link = link
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.now = NodeList(homepage)
        

    def visit(self, url: str) -> None:
        self.now.next = NodeList(url,None,self.now)
        self.now = self.now.next
        

    def back(self, steps: int) -> str:
        while self.now.prev and steps > 0:
            self.now = self.now.prev
            steps -=1
        return self.now.link
        

    def forward(self, steps: int) -> str:
        while self.now.next and steps > 0:
            self.now = self.now.next
            steps -=1
        return self.now.link
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)