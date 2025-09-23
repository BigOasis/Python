"""
프로그래머스 - 문자열 압축
45분
"""


def solution(s):
    n = len(s)
    if n == 1:
        return 1

    ans = n  # 현재까지 압축할 수 있는 가장 긴 문자열 일부 길이

    for sz in range(1, n // 2 + 1):
        comp = ""
        prev = s[:sz]
        cnt = 1

        for i in range(sz, n, sz):
            cur = s[i:i + sz]
            # 같으면 카운트 증가
            if cur == prev:
                cnt += 1
            # 다르면 prev에 저장
            else:
                if cnt > 1:
                    comp += str(cnt) + prev
                else:
                    comp += prev
                prev = cur
                cnt = 1
        # 마지막 저장
        if cnt > 1:
            comp += str(cnt) + prev
        else:
            comp += prev

        ans = min(ans, len(comp))
    return ans
