class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans  = [0] * n
        st = []
        for i in range(len(temperatures)):
            while st and st[-1][0] < temperatures[i]:
                t, ind = st.pop()
                ans[ ind] = (i - ind)
            st.append([temperatures[i],i])
        return ans
        