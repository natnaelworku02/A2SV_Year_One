class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) ==1:
            return ""
        s = list(palindrome)
        a_count =  palindrome.count('a')
        for i in range(len(s)):
            if s[i] != 'a' and a_count - len(s) != -1:
                s[i] = 'a'
                break
            elif i== len(s) -1 and s[i] =='a':
                s[i] = 'b'
                break

        return ''.join(s)
        