import math


def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]


def is_prime(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    number = convert(n, k)
    parts = number.split('0')

    for part in parts:
        if part:
            num = int(part)
            if is_prime(num):
                answer += 1

    return answer