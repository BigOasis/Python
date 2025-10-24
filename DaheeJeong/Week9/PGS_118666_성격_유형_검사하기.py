def solution(players, m, k):
    answer = 0
    server = [m] * (len(players))

    for i, player in enumerate(players):
        if player >= server[i]:
            diff = player + 1 - server[i]
            server_num = diff // m

            if diff % m != 0 or diff == 0:
                server_num += 1

            length = i + k
            if length > 24:
                length = 24

            for j in range(i, length):
                server[j] += server_num * m
            answer += server_num

    return answer
