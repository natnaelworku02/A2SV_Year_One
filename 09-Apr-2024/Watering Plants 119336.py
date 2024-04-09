# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=0
        cap =capacity
        for i,p in  enumerate (plants):
            if p> cap:
                step+=2*i
                cap=capacity
            step+=1
            cap-=p
        return step
