def binary_search_iter(seq, target):
    high, low = len(seq), 0 #15 0
    while low < high:
        mid = (high + low) // 2 # 7, 3
        if target == seq[mid]: # 2==5
            return mid
        elif target < seq[mid]: # 2<5
            high = mid # 7
        else:
            low = mid + 1
    return None

def intersection_two_arrays_sets(seq1,seq2):
    set1 = set(seq1)
    set2 = set(seq2)
    return set1.intersection(set2)

def intersection_two_arrays_ms(seq1_ori, seq2_ori):
    seq1=seq1_ori[:]
    seq2=seq2_ori[:]
    res=[]
    while seq1 and seq2:
        if seq1[-1]==seq2[-1]:
            res.append(seq1.pop())
            seq2.pop()
        elif seq1[-1]>seq2[-1]:
            seq1.pop()
        else:
            seq2.pop()
    res.reverse()
    return res

def intersection_two_arrays_bs(seq1, seq2):
    if len(seq1)>len(seq2):
        seq, key = seq1, seq2
    else:
        seq, key = seq2, seq1
    intersec=[]
    for item in key:
        if binary_search_iter(seq,item):
            intersec.append(item)
    return intersec

def test_intersection_two_arrays():
    seq1 = [1,2,3,5,7,8]
    seq2 = [3,5,6]
    assert(set(intersection_two_arrays_sets(seq1,seq2))==set([3,5]))
    assert(set(intersection_two_arrays_ms(seq1,seq2))==set([3,5]))
    assert(set(intersection_two_arrays_bs(seq1,seq2))==set([3,5]))
    print("테스트 통과!")

if __name__=='__main__':
    test_intersection_two_arrays()