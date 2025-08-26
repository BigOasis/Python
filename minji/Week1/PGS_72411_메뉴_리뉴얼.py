from itertools import combinations   # 조합 뽑기
from collections import Counter      # 횟수 세기

def solution(orders, course):
    answer = []  # 최종 결과리스트 (각각 코스별로 가장 많이 나온 조합을 answer에 추가했음)

    # 1. 코스 길이 하나씩 확인 (예: 2, 3, 4)
    for length in course:
        all_combi = []  # 현재 길이에서 나온 모든 조합 저장

        # 2. 손님 주문마다 조합 뽑기
        for order in orders:
            sorted_order = sorted(order)  # 알파벳 순 정렬 (순서 통일)
            combos = combinations(sorted_order, length)  # combinations로 조합 생성 시 다 (튜플)로 만들어짐!
            # sorted_order = ['A','B','C']라고 하면 length가 2일때 combinations로 조합 생성 한 결과인 combo는 [('A','B'), ('A','C'), ('B','C')]가 됨

            for combo in combos:
                # combo는 ('A','B') 같은 튜플 형태이기때문에 ''.join(('A','B')) → "AB" (문자열로 합쳐서 저장)
                all_combi.append(''.join(combo))

        # 3. 이번 코스 길이에서 조합이 하나도 안 나오면 건너뜀
        if not all_combi:
            continue

        # 4. 조합별 등장 횟수 세기 (등장 횟수가 동일한 애들이 있다면 같이 answer에 넣으면됨)
        menu_count = Counter(all_combi)
        # 예: {'AC': 4, 'BC': 2, 'CD': 2, ...}

        # 5. 가장 많이 주문된 횟수 구하기
        max_count = max(menu_count.values())

        # 6. 최소 2번 이상 주문된 조합만 후보
        if max_count < 2:
            continue

        # 7. 가장 많이 주문된 조합만 결과에 추가
        for combo, freq in menu_count.items():
            if freq == max_count:
                answer.append(combo)

    # 8. 최종 결과를 사전 순으로 정렬
    return sorted(answer)
