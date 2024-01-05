class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = 0
        second = 0
        ans = []
        # skipped = None
        added =set()
        prev = 0
        while first < len(firstList) and second < len(secondList):
            x1,y1 = firstList[first]
            x2,y2 = secondList[second]
            xans = 0
            yans = -1
            
            if x2 >= x1:
                xans = x2
            else:
                 xans = x1
            if y2 <= y1 and y2 >=xans:
                yans = y2
                prev = y1
            elif y1 < y2 and y1 >= xans:
                yans = y1
                prev = y2
            if yans != -1 and (xans,yans) not in added:
                ans.append([xans,yans])
                added.add((xans,yans))
            
            if y1 <= y2:

                first += 1
            else:

                second += 1
        return ans

