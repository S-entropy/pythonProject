n = int(input())
lis = []
points = list(map(int, input().split()))
point = [i - 20 for i in points]
time = [0 for i in range(5)]
for i in range(5):
    number, p, q = map(int,input().split())
    lis.append([number,p,q])
lis.sort(key=lambda x : x[2]/x[1], reverse = True)
cur = 0
while cur<5:
    if point[lis[cur][0]]+lis[cur][2]<=100 and n-lis[cur][1]>=0:
        point[lis[cur][0]]+=lis[cur][2]
        n-=lis[cur][1]
        time[lis[cur][0]]+=lis[cur][1]
    else:
        cur+=1
print(*time)
print(*point)
print(sum(point)/5)