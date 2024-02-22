class Solution:
    def evalRPN(self, tokens) -> int:
        st = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                st.append(st.pop() + st.pop())
            elif tokens[i] == '-':
                st.append(-st.pop() + st.pop())
            elif tokens[i] == '*':
                st.append(st.pop() * st.pop())
            elif tokens[i] == '/':
                x = st.pop()
                y = st.pop()
                z=int(y / x)
                st.append(z)
            else:
                st.append(int(tokens[i]))

        return st.pop()