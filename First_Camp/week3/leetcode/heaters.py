class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        _min = 0
        _max = 10**9
        # print(_max)

        def helper(rad):
            ans = [0]*len(houses)
            i = 0
            j = 0
            while i < len(houses) and j < len(heaters):
                # print(heaters[j] + rad, heaters[j] - rad)
                if houses[i] <= heaters[j] + rad and houses[i] >= heaters[j] - rad:
                    ans[i] = 1
                    i +=1
                    # print(ans)
                else:
                    j +=1
            return False if ans.count(0) else True
        

        res = 0
        while _min <= _max:
            mid = (_min  + _max)//2

            bol = helper(mid)
            # print(mid,_min,_max)
            if bol:
                # print("hi")
                res = mid
                _max = mid -1
            else:
                _min = mid +1
        return res
             
