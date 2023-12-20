class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols,rows=0,0
        count=0
        while cols < len(strs[0]):
            while rows < len(strs)-1:
                if strs[rows][cols] > strs[rows+1][cols]:
                    count+=1

                    break


                rows+=1
            cols+=1
            rows=0
        return count
        

        