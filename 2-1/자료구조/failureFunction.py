def fail(pat):
    n = len(pat)
    failure = [-1]
    for j in range(1,n):
        i = failure[j-1]
        while pat[j] != pat[i+1] and i>=0:
            i = failure[i]
        if pat[j] == pat[i+1]:
            failure.append(i+1)
        else:
            failure.append(-1)
    return failure
print(fail('ABABCABAB'))

def pmatch(str, pat):
    i=0
    j=0
    lens = len(str)
    lenp = len(pat)
    failure = fail(pat)
    while i < lens and j < lenp:
        if str[i] == pat[j]:
            i+=1
            j+=1
        elif j==0:
            i+=1
        else:
            j = failure[j-1] + 1
    if j==lenp:
        return i-lenp
    else:
        return -1