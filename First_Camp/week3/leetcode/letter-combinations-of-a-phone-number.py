class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        di = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}
        ans = []
        def helper(ind,path):
            if ind == len(digits):
                ans.append(''.join(path.copy()))
                return
            for value in di[digits[ind]]:
                path.append(value)
                helper(ind+1,path)
                path.pop()
        if not digits:
            return []
        helper(0,[])
        return ans

