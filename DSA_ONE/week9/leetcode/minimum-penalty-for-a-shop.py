class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        y_arr = [0]*(n+1)
        y_sum = 0
        n_arr = [0] * (n+1)
        n_sum = 0

        for i in range(n):
            if customers[-1-i] == "Y":
                y_sum += 1
            if customers[i] == "N":
                n_sum += 1
            n_arr[i+1] = n_sum
            y_arr [-2-i] = y_sum
        ans = [float("inf"),-1]
        # print(y_arr , n_arr)
        for i in range(n+1):
            if ans[0]  > y_arr[i]+ n_arr[i]:
                ans[0] = y_arr[i]+n_arr[i]
                ans[1] = i
                # print(i,y_arr[i]+n_arr[i])
        return ans[1]

        

        