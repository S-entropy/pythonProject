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
print(countingSort([1,3,4,5,2,1,8,2,3,4,4,2,3,4,4,5]))
print(CSWithMaxv([1,3,4,5,2,1,8,2,3,4,4,2,3,4,4,5],8))
print(CSWithNegN([-1,0,3,4,5,2,-10,5,2,5,2,4,4,2,3,6]))