'''
import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        print(f"{func.__name__} 함수 실행 시간: {e - s}초")
        return result
    return wrapper


def memo(func):
    cache = {}


    # @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#데커레이터 사용
@memo
def fib2(n):
    if n < 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


def fib3(m, n):
    if m[n] == 0:
        m[n] = fib3(m, n-1) + fib3(m, n-2)
    return m[n]


@timer_decorator
def test_fib(n):
    print(fib(n))


@timer_decorator
def test_fib2(n):
    print(fib2(n))


@timer_decorator
def test_fib3(n):
    m = [0] * (n+1)
    m[0], m[1] = 1, 1
    print(fib3(m, n))


if __name__ == "__main__":
    n = 35
    test_fib(n)
    test_fib2(n)
    test_fib3(n)



# ver 1
def fib(num):
    # 탈출 조건
    if num < 2:
        return num

    return fib(num - 1) + fib(num - 2)

num = int(input())
print(fib(num))

# ver 2
def fib(num):
    # 탈출 조건
    if dp[num] == -1: # 한번도 연산된 적이 없다면
        dp[num] = fib(num - 1) + fib(num - 2)

    return dp[num]

num = int(input())
dp = [-1] * 100
dp[0] = 0
dp[1] = 1
print(fib(num))
'''
# ver 3
num = int(input())
dp = [0] * 100
dp[1] = 1

for i in range(2, num + 1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[num])
