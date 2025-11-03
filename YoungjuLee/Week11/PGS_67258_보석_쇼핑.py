"""
프로그래머스 67258. 보석 쇼핑
풀이시간: 50분
"""


def solution(gems):
    num = len(set(gems))  # 전체 보석 종류 개수
    d = {}
    s = 0
    ans = [0, len(gems) - 1]  # 최소 구간 후보

    for e in range(len(gems)):
        d[gems[e]] = d.get(gems[e], 0) + 1  # 보석 개수 추가

        # 투포인터
        while len(d) == num:
            if e - s < ans[1] - ans[0]:
                ans = [s, e]

            d[gems[s]] -= 1
            if d[gems[s]] == 0:
                del d[gems[s]]
            s += 1
    # 시작 진열대 번호와 끝 진열대 번호를 1부터 시작하는 인덱스로 반환
    return [ans[0] + 1, ans[1] + 1]
