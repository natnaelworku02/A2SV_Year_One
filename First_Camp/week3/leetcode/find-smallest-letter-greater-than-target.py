class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left = 0
        right = len(letters) - 1
        ans = ''
        while left <= right:
            mid = (left + right)//2

            if letters[mid] > target:
                ans = letters[mid]
                right = mid -1
            elif letters[mid] < target:
                left = mid + 1
            else:
                
                while mid < len(letters) and letters[mid] == target:
                    mid +=1
                return letters[mid] if mid < len(letters) else  letters[0]
        return ans if ans != "" else letters[0]

                