from bisect import bisect_left, bisect_right
def binary_search_iter(seq, target):
    high, low = len(seq), 0
    while low < high:
        mid = (high + low) // 2
        if target == seq[mid]:
            return mid
        elif target < seq[mid]:
            high = mid
        else:
            low = mid + 1
    return None

def find_time_occurrence_list(seq,k):
    index_some_k = binary_search_iter(seq, k)
    count = 1
    sizet = len(seq)
    for i in range(index_some_k+1, sizet):
        if seq[i]==k:
            count+=1
        else:
            break
    for i in range(index_some_k-1,-1,-1):
        if seq[i]==k:
            count+=1
        else:
            break
    return count
def find_time_occurrence_list2(seq,k):
    return bisect_right(seq,k) - bisect_left(seq,k)
def test_find_time_occurrence_list():
    seq = [1,2,2,2,2,2,2,5,6,6,7,8,9]
    assert(find_time_occurrence_list(seq,2)==6)
    v = bisect_right(seq,2) - bisect_left(seq,2)
    assert(find_time_occurrence_list2(seq,2) == 6)
    print('테스트 통과!')

if __name__=='__main__':
    test_find_time_occurrence_list()