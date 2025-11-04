def solution(s):
    min_len, length = len(s), len(s)

    if len(s) == 1:
        return 1

    for i in range(1, length // 2 + 1):
        now = s[:i]
        cnt = 1
        result = ''

        for j in range(i, length, i):
            nxt = s[j:j + i]
            if nxt != now:
                if cnt == 1:
                    result += now
                else:
                    result += str(cnt) + now
                cnt = 1
                now = nxt
            else:
                cnt += 1

        if cnt == 1:
            result += now
        else:
            result += str(cnt) + now
        min_len = min(min_len, len(result))

    return min_len