from itertools import product

def solution(users, emoticons):
    # 각 이모티콘의 할인별 가격 미리 계산
    rates = [10, 20, 30, 40]
    discounted = [
        [price * (100 - r) // 100 for r in rates] 
        for price in emoticons
    ]

    best_sub = -1
    best_rev = -1

    # 모든 할인 배정 조합 탐색
    for choice in product(range(4), repeat=len(emoticons)):  
        sub_cnt = 0
        revenue = 0

        # 각 사용자에 대해 구매합 계산 
        for min_rate, limit_price in users:
            buy_sum = 0
            # min_rate 이상 할인된 이모티콘만 구매
            for idx, sel in enumerate(choice):
                if rates[sel] >= min_rate:
                    buy_sum += discounted[idx][sel]
            # 구매합이 한도 이상이면  취소하고 가입
            if buy_sum >= limit_price:
                sub_cnt += 1
            else:
                revenue += buy_sum

        # 1순위: 가입자 수 최댓값, 2순위: 매출 최댓값
        if sub_cnt > best_sub or (sub_cnt == best_sub and revenue > best_rev):
            best_sub, best_rev = sub_cnt, revenue

    return [best_sub, best_rev]