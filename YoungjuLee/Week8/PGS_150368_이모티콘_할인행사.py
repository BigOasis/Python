"""
프로그래머스 150368. 이모티콘 할인행사

풀이시간
풀이방법:
1. 이모티콘 플러스 서비스 가입자 최대화
    정가합 곱 비율보다 가격이 높아야 가입함
2. 이모티콘 판매액 최대화
    전부 가입하는것보다 일부 할인율을 조정해야함 => 조합?
"""
from itertools import product


def solution(users, emoticons):
    answer = [0, 0]  # [이모티콘 플러스 가입자 수, 총 판매액]
    # n = len(users)  # 유저 수
    m = len(emoticons)  # 이모티콘 수
    sales = [10, 20, 30, 40]  # 할인율(백분율)

    # 모든 할인 조합(4^7)
    for rates in product(sales, repeat=m):
        plus_cnt, total_sales = 0, 0

        # 할인율, 가격
        for disc, limit in users:
            total = 0
            for r, emo_price in zip(rates, emoticons):
                if r >= disc:  # 기준 할인 이상이면 구매
                    total += emo_price * (100 - r) / 100
            if total >= limit:  # 기준 가격 이상이면 이모티콘 플러스 가입
                plus_cnt += 1
            else:  # 아니면 그냥 토탈 금액으로 저하기
                total_sales += total
        if plus_cnt > answer[0] or (plus_cnt == answer[0] and total_sales > answer[1]):
            answer = [plus_cnt, total_sales]
    return answer
