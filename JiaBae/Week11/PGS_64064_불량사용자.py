def solution(user_id, banned_id):
    # 패턴 매칭 함수
    def match(u, p) -> bool:
        if len(u) != len(p):
            return False
        return all(pb == '*' or ub == pb for ub, pb in zip(u, p))

    # 각 불량 패턴별 후보 user 목록 미리 계산
    candidates = [[u for u in user_id if match(u, p)] for p in banned_id]

    # (선택지 줄이기용) 
    candidates.sort(key=len)

    used = set()             # 이미 사용한 user 아이디
    results = set()          # frozenset로 중복 제거

    def dfs(i, picked):
        if i == len(candidates):
            results.add(frozenset(picked))  # 순서 무시를 위해 frozenset 사용
            return
        for u in candidates[i]:
            if u in used: 
                continue
            used.add(u)
            picked.append(u)
            dfs(i + 1, picked)
            picked.pop()
            used.remove(u)

    dfs(0, [])
    return len(results)