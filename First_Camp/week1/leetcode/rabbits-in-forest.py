class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        di  = Counter(answers)
        ans = 0
        for key ,value in di.items():
            ans += ceil(value/(key +1)) * (key+1)
            
            
            

           
            
        return ans



        