def solution(id_list, report, k):
    report = list(set(report))  # 중복 제거

    user = {id: [] for id in id_list}  # 신고한 사람들 저장용
    count = {}  # 신고당한 횟수

    # 신고 관계 정리
    for r in report:
        a, b = r.split()
        user[a].append(b)
        count[b] = count.get(b, 0) + 1

    # 정지된 사람 찾기
    banned = []
    for name, c in count.items():
        if c >= k:
            banned.append(name)

    # 메일 몇 개 받는지 세고 리턴!
    answer = []
    for id in id_list:
        mail = 0
        for target in user[id]:
            if target in banned:
                mail += 1
        answer.append(mail)
    return answer
