class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo  = [0]*(amount+1)
        memo[0] = 1

        for i in range(len(coins)):
            for j in range(len(memo)):
                if j + coins[i] < len(memo):
                    memo[j + coins[i]] += memo[j]
            # print(memo)
            # print("________")
        
        return memo[-1]

