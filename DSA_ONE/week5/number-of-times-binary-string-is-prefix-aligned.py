class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # di = defaultdict(int)
        arr =  [0]*len(flips)
        count = 0
        _max = 0
        _ind_0 = 0
        for i in range (len(flips)):
            arr[flips[i]-1] = 1
            _max = max( flips[i]- 1,_max)
            ind=i
            while   _ind_0 <len(arr) and arr[flips[ind]-1] == arr[_ind_0]:
                # print(1)
                _ind_0 += 1 
                ind=0
                
            if  _ind_0 > _max :
                count += 1
        return count


        