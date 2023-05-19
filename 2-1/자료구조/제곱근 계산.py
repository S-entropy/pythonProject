def find_sqrt_bin_search(n,error=0.001):
    lower = n<1 and n or 1
    upper = n<1 and 1 or n # n<1인 경우 고려한 코드.
    mid = lower + (upper-lower) / 2.0
    square = mid*mid
    while abs(square-n) > error:
        if square < n:
            lower = mid
        else:
            upper = mid
        mid = lower + (upper-lower) / 2.0
        square = mid * mid
    return mid

if __name__ =='__main__':
    a=2
    b=9
    import math
    print(math.sqrt(a))
    print(find_sqrt_bin_search(a))
    print(math.sqrt(b))
    print(find_sqrt_bin_search(b))