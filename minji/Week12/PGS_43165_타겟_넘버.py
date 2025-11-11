def solution(numbers, target):
    memo = {}  # (index, total) 경우의 수 저장
    return dfs(numbers, 0, 0, target, memo)

def dfs(numbers, index, total, target, memo):
    # 이미 계산한 상태면 캐시된 값 반환
    if (index, total) in memo:
        return memo[(index, total)]

    # 모든 숫자를 다 썼다면
    if index == len(numbers):
        return 1 if total == target else 0

    # 다음 단계 계산
    plus = dfs(numbers, index + 1, total + numbers[index], target, memo)
    minus = dfs(numbers, index + 1, total - numbers[index], target, memo)

    memo[(index, total)] = plus + minus
    return memo[(index, total)]
