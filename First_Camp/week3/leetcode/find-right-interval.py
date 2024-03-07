class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        pair = sorted([(val[0],i) for i,val in enumerate(intervals)])
        # print(pair)
        def search(val):
            ans = -1

            left = 0
            right = len(intervals) - 1

            while left <= right:
                mid = (left + right)//2
                # print(pair[mid][0],val)
                if pair[mid][0] == val:
                    ans = mid
                    break
                elif pair[mid][0] > val:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            # print(ans)
            return pair[ans][1] if ans != -1 else -1  


        data = []
        for i in range(len(intervals)):
            
            data.append(search(intervals[i][1]))
           
        return data

