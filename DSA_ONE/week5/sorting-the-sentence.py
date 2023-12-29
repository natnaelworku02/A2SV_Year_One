class Solution:
    def sortSentence(self, s: str) -> str:
        arr= s.split()
        
        arr.sort(key= lambda x : int(x[-1]))
        # for i in range(len(arr)):
        #     ind = i
        #     for j in range(i+1,len(arr)):
        #         if arr[j][-1] < arr[ind][-1]:
        #             ind = j
        #     if ind != i:
        #         arr[i], arr[ind] = arr[ind], arr[i]
        for i in range(len(arr)):
            arr[i]= arr[i][:-1]

        return ' '.join(arr)
        


        