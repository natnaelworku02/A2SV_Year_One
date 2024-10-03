class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        nums = []

        for ch in s:
            # print(ord(ch), ord(ch) - 96, ch)
            val = str(ord(ch) - 96)
            val = [i for i in val]
            nums.extend(val)
        
        # ans = 0
        # print(nums)
        for i in range(k):
            temp = 0
            for val in nums:
                temp += int(val)
            # print(temp)
            temp = str(temp)
            nums = [i for i in temp]
        
        return int(''.join(nums))
