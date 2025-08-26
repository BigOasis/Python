from itertools import combinations # 조합 쓸려고 사용
from collections import Counter # 갯수 셀려고 사용

def solution(orders, course):
    answer = []
    max_values = [] # course 길이별 최대 조합 리스트
    menus = [] # 메뉴 조합 리스트

    for combi_len in course: # course 순회하며 모든 조합 찾기
        menu_list = []
        for order in orders: # orders 순회하며 가능한 조합 모두 찾기
            menu_list += list(combinations(sorted(order), combi_len))
        count_dict = Counter(menu_list) # Counter를 사용하면, dict가 나온다
        
        for k, v in count_dict.items(): # 하나씩 순회하며 셀 것입니다
            if v >= 2 and v == max(count_dict.values()): # count_dict에서 가장 큰 "value"이고, 그것이 2보다 크다면
                answer.append(''.join(k)) # 그것은 정답이올시다
        
    return sorted(answer) # 정답은, 알파벳 오름차순으로 정렬해야 할 것이다