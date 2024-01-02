class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        # i=0
        count =0
        # print(costs)
        for i in range(len(costs)):
            if coins - costs[i] >=0:
                count+=1
                coins -= costs[i]
            else:
                break
        return count

        