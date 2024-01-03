class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        su=0
        while l<=r:
            if l==r:
                su+=1
                break
            if people[l]+people[r] <= limit:
                su+=1
                l+=1
                r-=1
            else:
                su+=1
                r-=1 

        return su





        