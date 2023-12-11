class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        temp=0
        for num in nums:
            if num%2==0:
                temp+=num
        for i in range (len(queries)):
            before=nums[queries[i][1]]
            nums[queries[i][1]]+=queries[i][0]
            if before %2==0:
                temp-=before

            if nums[queries[i][1]]%2==0:
                temp+=nums[queries[i][1]]
            ans.append(temp)
            
            
        return ans if ans else [0]*len(queries)