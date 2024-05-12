class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans =[]
        for i in range(len(grid) - 2):
            temp =[]
            for j in range(len(grid[0]) - 2):
                r  = i
                c = j
                _max =0
                for i_ind in range(3):
                    for j_ind in range(3):
                        _max= max(_max,grid[r+i_ind][c+j_ind])
                temp.append(_max)
            ans.append(temp)
        return ans

