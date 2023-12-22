class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        di= defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                di[i+j].append(mat[i][j])
        answer=[]
        for key,value in di.items():
            if key%2==0:
                answer.extend(value[::-1])
            else:
                answer.extend(value)
        return answer
        




