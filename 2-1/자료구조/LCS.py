a=input()
b=input()
cur = [0 for _ in range(len(b)+1)]
l = [cur[:] for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1]==b[j-1]:
            l[i][j]=l[i-1][j-1]+1
        else:
            l[i][j]=max(l[i][j-1], l[i-1][j])
print(l[-1][-1])
x = len(a)
y = len(b)
string = []
while True:
    if x>1 and l[x][y] == l[x-1][y]:
        x = x-1
    elif y>1 and l[x][y] == l[x][y-1]:
        y = y-1
    else:
        string.append(a[x-1])
        x = x-1
        y = y-1
    if l[x][y]==0:
        break
string.reverse()
string = ''.join(string)
print(string)