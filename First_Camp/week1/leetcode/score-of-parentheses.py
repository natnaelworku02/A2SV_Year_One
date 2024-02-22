class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # ans = 0
        st = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append('(')
            else:
                # print(st)
                val = 0
                if st[-1] == '(':
                    print("hi")
                    st.pop()
                    val = 1

                elif st[-1].isdigit():
                    
                    val = int(st.pop())
                    if st and  st[-1] =='(':
                        st.pop()
                        val = val * 2
                while st and  st[-1].isdigit() :
                    val += int(st.pop())
                st.append(str(val))       
        # print(temp,ans)
        return int(st.pop())