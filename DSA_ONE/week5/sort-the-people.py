class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            ind=i
            for j in range(i+1,len(names)):
                if heights[j] > heights[ind]:
                    ind=j
            if ind != i:
                heights[ind] , heights[i] = heights[i] , heights[ind]
                names[ind] , names[i] = names[i] , names[ind]
        # print(heights)
        return names

        