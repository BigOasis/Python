def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    # 1. k진수로 변환
    result = ''
    while n > 0:
        result = str(n % k) + result
        n //= k
    
    # 2. 0 기준으로 나누기
    parts = result.split('0')
    
    # 3. 소수 개수 세기
    answer = 0
    for p in parts:
        if p != '' and is_prime(int(p)):
            answer += 1
    return answer
