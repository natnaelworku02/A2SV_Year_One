class Solution:
    def minimumPushes(self, word: str) -> int:
        
        di = defaultdict(int)

        count = Counter(word)
        count = count.most_common()

        # print(count)
        

        num = 1

        items = 0
        ans = 0

        for key,val in count:
            
            ans += val*num
            items += 1

            if items == 8:
                items = 0
                num += 1
        
        return ans
