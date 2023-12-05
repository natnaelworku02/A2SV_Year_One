class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        goal=0
        goal=(abs(target[0]-0)+abs(target[1]-0))
        data_list=[]
        for i in range(len(ghosts)):
           data_list.append(abs(target[0]-ghosts[i][0])+abs(target[1]-ghosts[i][1])) 
        min_data=min(data_list)
        if min_data>goal:
            return True
        return False

        