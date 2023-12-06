class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        length=len(list1)+len(list2)
        answer=[]
        for i,element in enumerate(list1):
            if element in list2:
                index_sum=i+list2.index(element)
                if length>index_sum:
                    answer.clear()
                    answer.append(element)
                    length=index_sum
                elif length == index_sum:
                    answer.append(element)
                    
                
        return answer

                
        