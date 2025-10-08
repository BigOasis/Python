"""
프로그래머스 k 진수에서 소수 개수 구하기

"""


def is_prime(x):
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        # 나누어 떨어지면 소수 X
        if x % i == 0:
            return False
    return True


def solution(n, k):
    s = ""
    # n을 k진수로 변환
    while n:
        s = str(n % k) + s
        n //= k
    nums = []

    for x in s.split('0'):
        if x:
            nums.append(int(x))
    cnt = 0

    for x in nums:
        if is_prime(x):
            cnt += 1
    return cnt
