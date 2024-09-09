class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                Flag = False
                if (i < len(flowerbed) - 1 and flowerbed[i+1] != 1) and (i > 0 and flowerbed[i-1] != 1):
                    # print(i)
                    count +=1 
                    flowerbed[i] = 1
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    count +=1
                    flowerbed[i] = 1
                elif i == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
        # print(count)
        # print(flowerbed)
        if count >= n:
            return True
        return False

