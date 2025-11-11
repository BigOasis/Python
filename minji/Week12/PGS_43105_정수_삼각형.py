def solution(triangle):
    # 아래에서 두 번째 줄부터 위로 올라오면서 갱신
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])

    return triangle[0][0]