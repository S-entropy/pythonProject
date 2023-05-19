l1 = input()
l2 = input()
cnt=0
for i in range(len(l2)-len(l1)+1):
	cur = l2[i:i+len(l1)]
	flg=True
	for i in l1:
		if l1.count(i)!=cur.count(i):
			flg=False
			break
	if flg:
		cnt+=1
print(cnt)