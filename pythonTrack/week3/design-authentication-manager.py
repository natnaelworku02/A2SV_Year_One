class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.setTimeOut=timeToLive
        self.tokens={}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId]=currentTime+self.setTimeOut
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId]=currentTime+self.setTimeOut
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for value in self.tokens.values():
            if value>currentTime:
                count+=1
        return count
            
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)