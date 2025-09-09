def solution(places):
    answer = []
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def bfs(a):
        for i in range(5):
            for j in range(5):
                if places[a][i][j] == 'P':
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if x < 0 or y < 0 or x >= 5 or y >= 5:
                            continue
                        if places[a][x][y] == 'O':
                            for l in range(4):
                                nx = x + dx[l]
                                ny = y + dy[l]
                                if nx == i and ny == j:
                                    continue
                                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                                    continue
                                if places[a][nx][ny] == 'P':
                                    return 0
                        else:
                            if places[a][x][y] == 'P':
                                return 0
        return 1

    for a in range(5):
        answer.append(bfs(a))

    return answer
