def find_elem_matrix_bool(m1, value):
    found = False
    row=0
    col = len(m1[0])-1
    while row < len(m1) and col>=0:
        if m1[row][col]==value:
            found = True
            break
        elif m1[row][col] > value:
            col-=1
        else:
            row+=1
    return found
def test_find_elem_matrix_bool():
    m1 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    assert(find_elem_matrix_bool(m1,8) is True)
    assert(find_elem_matrix_bool(m1,3) is False)
    m2=[[0]]
    assert(find_elem_matrix_bool(m2,0) is True)
    print("테스트 통과!")

if __name__=='__main__':
    test_find_elem_matrix_bool()