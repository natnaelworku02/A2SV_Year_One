class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        while right > left:
            right = right & (right -1)
        #     print(right)
        # print(right)
        return right