'''
n = int(input())
l = list(map(int,input().split()))
dp = []
dp.append(l[0])
dp.append(max(l[0],l[1]))
for i in range(2, n):
    dp.append(max(dp[i-1], dp[i-2]+l[i]))
print(dp[-1])
'''
n = int(input())
l = list(map(int,input().split()))
dp = []
dp.append(l[0])
dp.append(l[1])
dp.append(l[0]+l[2])
for i in range(3, n):
    dp.append(max(dp[i-2], dp[i-3])+l[i])
print(max(dp[-1], dp[-2]))