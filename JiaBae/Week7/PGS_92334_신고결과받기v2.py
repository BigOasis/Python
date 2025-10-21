from collections import defaultdict

def solution(id_list, report, k):
    # report를 해시맵으로 기록
    report_hashmap = defaultdict(set)
    
    for r in report:
        reporter, reported = r.split()
        report_hashmap[reporter].add(reported)
    
    # 신고당한 횟수 기록 해시맵
    reported_hashmap = defaultdict(int)
    for v in report_hashmap.values():
        for item in v:
            reported_hashmap[item] += 1

    # 정지되는 유저 목록
    banned = [user for user, v in reported_hashmap.items() if v >= k ]
    
    answer = []
    for id in id_list:
        cnt = 0
        for reported in report_hashmap[id]:
            if reported in banned:
                cnt += 1
        answer.append(cnt)
        
    return answer