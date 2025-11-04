from collections import defaultdict

def solution(gems):
    answer = [0, len(gems) - 1]
    
    # 종류 가짓수 
    totals = len(set(gems))
    d = defaultdict(int)
    left = 0
    n = len(gems)
    
    for right in range(n):
        d[gems[right]] += 1
        
        while len(d) == totals:
            # 최소 길이 갱신
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            
            # 왼쪽 이동
            d[gems[left]] -= 1
            if d[gems[left]] == 0:
                del d[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1] + 1]