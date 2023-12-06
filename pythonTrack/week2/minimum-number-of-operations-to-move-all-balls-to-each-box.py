class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer=[0]*len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    answer[i]+=abs(j-i)
        return answer
        