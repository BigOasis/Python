def solution(survey, choices):
    answer = ''
    length = len(survey)
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(length):
        if choices[i] <= 4:
            dic[survey[i][0]] += 4 - choices[i]
        else:
            dic[survey[i][1]] += choices[i] - 4

    lst = list(dic.items())

    for i in range(0, 8, 2):
        if lst[i][1] < lst[i + 1][1]:
            answer += lst[i + 1][0]
        else:
            answer += lst[i][0]

    return answer