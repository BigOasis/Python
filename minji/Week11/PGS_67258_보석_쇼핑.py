def solution(gems):
    N = len(gems)
    answer = [0, N-1]
    kind = len(set(gems))  # 보석종류
    dic = {gems[0]:1,}  # 종류 체크
    start,end = 0,0 
    while start<N and end<N:
        if len(dic) < kind:  # 종류가 다 안모였으면 end 증가 & dic 개수 ++
            end += 1
            if end == N:
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1

        else:  # 종류 같으면 ans 비교 후 답 갱신하고, start 증가 & dic 개수 --
            if (end-start+1) < (answer[1]-answer[0]+1):
                answer = [start,end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

    answer[0] += 1
    answer[1] += 1
    return answer