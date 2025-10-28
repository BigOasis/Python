def fork(storage, box, n, m):  # 지게차
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    remove_st = []

    for i in range(1, n+1):
        for j in range(1, m+1):
            if storage[i][j] == box:
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if storage[ni][nj] == "0":
                        remove_st.append((i, j))
                        break

    for i, j in remove_st:
        storage[i][j] = "0"
        spread_outside(storage, i, j)

def crane(storage, box, n, m):  # 크레인
    for i in range(1, n+1):
        for j in range(1, m+1):
            if storage[i][j] == box:
                storage[i][j] = "1"
                spread_outside(storage, i, j)

def spread_outside(storage, x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    if any(storage[x + dx[k]][y + dy[k]] == "0" for k in range(4)): # 외부와 이어지는가?
        storage[x][y] = "0"
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k] 
            if storage[nx][ny] == "1": # 0으로 만든 뒤 다른것들도 외부와 이어지는지?
                spread_outside(storage, nx, ny)

def solution(storage, requests):
    answer = 0
    m = len(storage[0])
    n = len(storage)
    
    storage = [list("0" + row + "0") for row in storage] # 외부를 0으로 만들어주기(둘러싸도록)
    storage.insert(0, list("0" * (m+2)))
    storage.append(list("0" * (m+2)))

    for req in requests:
        if len(req) == 1:
            fork(storage, req, n,m)
        else:
            crane(storage, req[0], n, m)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if storage[i][j] not in ["0", "1"]:
                answer += 1
    return answer