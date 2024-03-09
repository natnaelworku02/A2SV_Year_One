class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.ballot=defaultdict()
        self.times=times
        self.persons=persons
        self.votes=defaultdict(int)
        current_maxV=0
        current_minV=0

        for per,ti in zip(self.persons,self.times):
            self.votes[per]+=1
            if self.votes[per] >= current_maxV:
                current_maxV=self.votes[per]
                current_minV=per
            self.ballot[ti]=current_minV


    def q(self, t: int) -> int:
        return self.ballot[self.times[bisect_right(self.times,t)-1]]
        
                
         


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)