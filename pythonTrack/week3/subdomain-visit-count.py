class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # dictionary to save each subdomain as key and pair value eith its call time
        subdomain=defaultdict(int)
        # loop to iterate for each cpdomain values
        for domain in cpdomains:
            num,sttr=domain.split()
            num=int(num)
            # loop to add value to subdomain based on there accessed time and subdomain name
            while '.' in sttr:
                subdomain[sttr]+=num
                sttr=sttr[sttr.index('.')+1:]
            subdomain[sttr]+=num
        answer=[]
        # assign teh value into an array so that it could be returned
        for key,value in subdomain.items():
            answer.append(str(value)+" "+key)
        return answer


        