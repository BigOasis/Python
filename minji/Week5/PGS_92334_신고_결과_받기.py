def solution(id_list, report, k):
    report = set(report)  # 중복 제거
    reported_count = {user: 0 for user in id_list}  # 신고당한 횟수
    mail_count = {user: 0 for user in id_list}      # 메일 받은 횟수
    
    # 신고당한 횟수
    for r in report:
        a, b = r.split()
        reported_count[b] += 1
    
    # 정지된 유저 찾기
    banned = [user for user, cnt in reported_count.items() if cnt >= k]
    
    # 내가 신고한 사람 중 정지된 사람이 있으면 메일++
    for r in report:
        a, b = r.split()
        if b in banned:
            mail_count[a] += 1
    
    # 결과는 id_list 순서대로
    return [mail_count[user] for user in id_list]
