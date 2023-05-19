def serching_in_a_matrix(m1, value):
    rows = len(m1)
    cols = len(m1[0])
    low = 0
    high = rows*cols # rows*cols-1
    while low<high:
        mid = (low+high)//2
        row = mid//cols
        col = mid%cols
        v = m1[row][col]
        if v==value:
            return True
        elif v>value:
            high = mid # mid-1
        else:
            low = mid+1
    return False

def test_searching_in_a_matrix():
    a = [[1,3,5],[7,9,11],[13,15,17]]
    import numpy
    b = numpy.array([(1,2),(3,4)])
    c =[[3]]
    assert(serching_in_a_matrix(a,13) is True)
    assert(serching_in_a_matrix(a,14) is False)
    assert(serching_in_a_matrix(b,3) is True)
    assert(serching_in_a_matrix(b, 5) is False)
    print("테스트 통과!")
if __name__ == "__main__":
    test_searching_in_a_matrix()