from collections import defaultdict

def solution(survey, choices):
    score = defaultdict(int)

    for s, c in zip(survey, choices):
        if c == 4:
            continue  # 점수 없음
        if c < 4:  # 비동의 계열: 왼쪽 문자에 (4 - c)점
            score[s[0]] += 4 - c     
        else:      # 동의 계열: 오른쪽 문자에 (c - 4)점
            score[s[1]] += c - 4 

    result = []
    for a, b in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        result.append(a if score[a] >= score[b] else b)

    return ''.join(result)