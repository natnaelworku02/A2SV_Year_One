class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pre = [0]* len(s)

        add = 0
        for i,char in enumerate(s):
            if char == '|':
                add +=1
            pre[i] = add
        res = []
        print(pre)
        for left,right in queries:
            if left + 1 >= right:
                res.append(0)
                continue
            numleft = bisect_left(pre,pre[left] + 1) if s[left]!= '|' else left
            numright = bisect_right(pre , pre[right] - 1) if s[right] != '|' else right
            count = 0
            lc = pre[numleft]
            leftdiff = numleft
            ind = numleft
            print(numleft,numright)
            if numleft >= numright:
                res.append(0)
            else: 
                while numleft <= numright:
                    mid = (numleft + numright)//2

                    if pre[mid] == lc:
                        numleft = mid + 1
                        
                    elif pre[mid] > lc:
                        count += pre[mid] - lc
                        lc = pre[mid]
                        ind = mid
                        numleft = mid + 1
                print(count,numleft,ind)
                res.append(ind  - leftdiff - count)
        return res