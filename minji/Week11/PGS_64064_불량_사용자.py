import re

def solution(user_id, banned_id):
    candidates = [] # 각 banned_id에 매칭되는 user_id 후보군들
    for b in banned_id:
        pattern = re.compile('^' + b.replace('*', '.') + '$')
        possible = {u for u in user_id if pattern.match(u)}
        candidates.append(possible)

    result = [set()]

    for c in candidates:
        new_result = [] # 이번 후보군까지 포함한 새로운 조합들
        for chosen in result:
            for u in c:
                if u not in chosen:
                    new_result.append(chosen | {u}) 
        result = new_result

    # 중복 조합 제거 (frozenset으로 불변화)
    unique = {frozenset(r) for r in result}
    return len(unique)
