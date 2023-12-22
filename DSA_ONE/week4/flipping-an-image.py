class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # for loop to make the row value reverse of the original
        for i in range(len(image)):
            
            image[i].reverse()
        #  travers to each index and change the bit to its complementary value
        for i in range(len(image)):
            
            for j in range(len(image[0])):
            
                image[i][j] = 1 - image[i][j]
        
        return image
            
        