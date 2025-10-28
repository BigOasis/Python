def solution(players, m, k):
    server = []
    for player in players:
        total = sum((server + [1])[-k:]) * m

        if total > player:
            server.append(0)
        else:
            server_num = (player - total) // m + 1
            server.append(server_num)

    return sum(server)