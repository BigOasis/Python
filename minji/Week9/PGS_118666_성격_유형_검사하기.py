def solution(survey, choices):
    # 각 성격 유형 점수 저장용 딕셔너리
    scores = {ch: 0 for ch in 'RTCFJMAN'}

    # 설문 결과에 따라 점수 누적
    for s, c in zip(survey, choices):
        left, right = s[0], s[1]
        if c < 4:  # 비동의 → 왼쪽 유형 점수
            scores[left] += 4 - c
        elif c > 4:  # 동의 → 오른쪽 유형 점수
            scores[right] += c - 4

    # 최종 유형 계산
    result = ''
    for a, b in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        result += a if scores[a] >= scores[b] else b

    return result