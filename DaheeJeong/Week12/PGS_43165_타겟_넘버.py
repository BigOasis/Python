def solution(numbers, target):
    cnt = 0

    def dfs(current, idx):
        nonlocal cnt
        if idx == len(numbers):
            if current == target:
                cnt += 1
            return

        dfs(current + numbers[idx], idx + 1)
        dfs(current - numbers[idx], idx + 1)

    dfs(0, 0)
    return cnt