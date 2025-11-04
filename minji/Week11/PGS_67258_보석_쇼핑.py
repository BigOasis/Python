def solution(gems):
    N = len(gems)
    kind = len(set(gems))
    dic = {}
    answer = [0, N - 1]
    start = 0

    for end in range(N):
        # 보석 추가
        dic[gems[end]] = dic.get(gems[end], 0) + 1

        while len(dic) == kind:
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]

            # 왼쪽 보석 제거하며 윈도우 축소
            dic[gems[start]] -= 1
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1

    # 1-based 인덱스로 변환
    return [answer[0] + 1, answer[1] + 1]
