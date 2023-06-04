n = int(input())
num = int('4' * n)
cnt = 0
ans = []
for i in range(2 ** n):
    v = int(str(bin(i))[2:])
    if (v + num) % 45 == 0:
        ans.append(v + num)
        cnt += 1
print(cnt)