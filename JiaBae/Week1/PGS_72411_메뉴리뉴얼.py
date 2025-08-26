from itertools import combinations

def solution(orders, course):
    answer = []
    
    # 각 주문 정렬
    orders = [''.join(sorted(o)) for o in orders]
    
    # 조합이 몇번 나왔는지 세는 해시맵
    subset_counter = {}
    
    # 모든 order에 대해 크기가 2 이상인 부분 집합 찾기
    for order in orders :
        for k in course :
            for comb in combinations(order, k) :
                if comb in subset_counter :
                    subset_counter[comb] += 1
                else:
                    subset_counter[comb] = 1
    
    # 단품메뉴 갯수에 따라 2명 이상한테 받은 조합 중 가장 많은 조합 찾기 
    for c in course :
        max_cnt = 0
        temp = []
        for sub in subset_counter :
            if len(sub) == c :
                if subset_counter[sub] > max_cnt :
                    max_cnt = subset_counter[sub]
                    temp = ["".join(sub)]
                elif subset_counter[sub] == max_cnt :
                    temp.append("".join(sub))
        if max_cnt >= 2 :
            answer.extend(temp)
    
    return sorted(answer)