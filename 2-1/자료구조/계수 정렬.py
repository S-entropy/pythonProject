def countingSort(l):
    m = max(l)
    cntl = [0] * (m + 1)
    for i in l:
        cntl[i] += 1
    ret = []
    for i in range(len(cntl)):
        for j in range(cntl[i]):
            ret.append(i)
    return ret
def CSWithMaxv(l, m):
    cntl = [0]*(m+1)
    for i in l:
        cntl[i]+=1
    ret = []
    for i in range(len(cntl)):
        for j in range(cntl[i]):
            ret.append(i)
    return ret
def CSWithNegN(l):
    M = max(l)
    m = min(l)
    cntl = [0]*(M-m+1)
    for i in l:
        cntl[i-m] += 1
    ret = []
    for i in range(len(cntl)):
        for j in range(cntl[i]):
            ret.append(i+m)
    return ret
print(countingSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))