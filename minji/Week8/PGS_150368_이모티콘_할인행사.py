# 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
# 이모티콘 판매액을 최대한 늘리는 것

# 중첩 반복문 대신 모든 조합을 한 번에 생성해주는 함수
from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    max_plus, max_sales = 0, 0

    # 모든 할인율 조합 생성
    for case in product(discount_rates, repeat=len(emoticons)):
        plus_cnt, sales = 0, 0 # 가입자 수, 판매액

        # 각 사용자 별 구매 여부 판단
        for user_rate, user_limit in users:
            total = 0

            # 이모티콘 모두 할인율 적용해보기
            for i in range(len(emoticons)):
                # 사용자 기준보다 할인율이 높으면 구매대상
                if case[i] >= user_rate:
                    total += emoticons[i] * (100 - case[i]) / 100
            if total >= user_limit:
                plus_cnt += 1
            else:
                sales += total
                
        # 최대 가입자 수, 최대 판매액 갱신
        if plus_cnt > max_plus or (plus_cnt == max_plus and sales > max_sales):
            max_plus, max_sales = plus_cnt, sales

    return [max_plus, int(max_sales)]
