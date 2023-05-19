def union_set(a,b):
    return a|b
def intersection_set(a,b):
    return a&b
def difference_set(a,b):
    return a-b
U = {1,2,3,4,5,6,7,8,9}
A = {1,2,3,4,5}
B = {1,3,5,7,9}
print(A)
print(difference_set(U,A))
print(union_set(A,B))
print(intersection_set(A,B))

print(difference_set(A,B))
print(difference_set(B,A))

a = set(map(int,input().split()))
b = set(map(int,input().split()))
s = union_set(a,b)-intersection_set(a,b)
print(s, len(s), max(s))