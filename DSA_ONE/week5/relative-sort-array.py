class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ind=0
        for num in arr2:
            for i in range(len(arr1)):
                if arr1[i] == num:
                    arr1[i],arr1[ind] = arr1 [ind] , arr1[i]
                    ind+=1
        # print(arr1[ind:])
        for i in range(ind,len(arr1)):
            index=i
            for j in range(index+1, len(arr1)):
                if arr1[j] < arr1[index]:
                    index=j
            if index != i:
                arr1[index] , arr1[i] =arr1[i], arr1[index]

        return arr1
        

        