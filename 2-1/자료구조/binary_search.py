# 재귀함수로 완성해 보세요. seq는 리스트, target은 찾을 값
def binary_search_rec(seq, target, low, high):
    if low > high:
        return None
    mid = (low + high)//2
    if seq[mid] == target:
        return mid
    elif seq[mid] > target:
        return binary_search_rec(seq, target, low, mid - 1)
    else:
        return binary_search_rec(seq, target, mid + 1, high)

# 반복문 형태로 코드를 완성해 보세요.
def binary_search_iter(seq, target):
    low = 0
    high = len(seq)-1
    while low <= high:
        mid = (high+low) // 2
        if seq[mid] == target:
            return mid
        elif seq[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

def test_binary_search():
    seq = [1, 2, 5, 6, 7, 10, 12, 12, 14, 15]
    target = 6
    assert(binary_search_iter(seq, target) == 3)
    assert(binary_search_rec(seq, target, 0, len(seq)-1) == 3)
    print("테스트 통과!")

if __name__ == "__main__":
    test_binary_search()

from bisect import bisect_left, bisect_right
l = list(map(int,input().split()))
l.sort()
print(len(l)-bisect_left(l, 80))
import bisect

result = []
for score in [33, 99, 77, 70, 89, 90, 100]:
    pos=bisect.bisect([60,70,80,90], score)
    grade = 'FDCBA'[pos]
    result.append(grade)
print(result)