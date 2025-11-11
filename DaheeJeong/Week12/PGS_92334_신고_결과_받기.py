def solution(id_list, report, k):
    answer = []
    a = list(set(report))

    dic1 = {name: [] for name in id_list}
    dic2 = {name: 0 for name in id_list}

    for s in a:
        dic1[s.split()[1]].append(s.split()[0])

    for i in dic1:
        if len(dic1[i]) >= k:
            for j in dic1[i]:
                dic2[j] += 1

    for i in dic2:
        answer.append(dic2[i])

    return answer