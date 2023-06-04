n = int(input())
dp = [[0 for _ in range(9)] for v in range(n)]
dp[0][5]=1
for i in range(1, n):
    for j in range(9):
        dp[i][j] = dp[i-1][(j-4)%9] + dp[i-1][(j-5)%9]
print(dp[-1][0])