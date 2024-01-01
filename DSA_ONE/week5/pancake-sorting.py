class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        _max=len(arr)
        sorted_arr = sorted(arr)
        leng=len(arr)
        last_ind = 0
        if sorted_arr == arr:
            return []
        while len(arr[:leng - last_ind]) > 0:
            # print(leng - last_ind,arr[:leng - last_ind])
            ind= arr[:leng - last_ind].index(_max)
            # print(arr[:ind+1])
            arr[:ind+1] = arr[:ind +1 ][::-1]
            arr [:leng - last_ind] =arr[:leng - last_ind][::-1]
            ans.append(ind+1)
            ans.append(leng- last_ind)
            # print(arr)

            last_ind +=1
            if arr == sorted_arr:
                return ans
            _max-=1

            
        