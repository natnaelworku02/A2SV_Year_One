class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        di = Counter(words)
        for keys in di.keys():
            di[keys] = - di[keys]
        
        nums = list(di.items())
        for i in range(len(nums)):
            nums[i] = nums[i] [::-1]
            # nums[i][0] = - nums[i][0]
        heapify(nums)
        
        # print(nums)

        ans = []
        for i in range(k):
            _,val = heappop(nums)
            ans.append(val)
        
        return ans
