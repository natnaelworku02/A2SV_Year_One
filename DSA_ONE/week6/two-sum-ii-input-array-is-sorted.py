class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        l=0
        r=len(numbers)-1
        while l<r:
            two=numbers[l]+numbers[r]
            if two>target:
                r-=1
            elif two<target:
                l+=1
            else:
                return [l+1,r+1]