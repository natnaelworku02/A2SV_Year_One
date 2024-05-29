class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        final_xor = 0

        for num in nums:
            final_xor ^= num
        ind = -1
        for i in range(31,-1,-1):
            if final_xor & 1<< i:
                ind = i
                break
            
        one = 0
        zero = 0

        for num in nums:

            if num & 1<<ind:
                one ^= num
            else:
                zero ^= num
        
        return [one,zero]