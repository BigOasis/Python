from itertools import product

def solution(users, emoticons):
    answer = []
    discount_list = [10, 20, 30, 40]

    for case in product(discount_list, repeat=len(emoticons)):
        result = [0, 0]
        for user in users:
            tmp = 0
            for idx, sale in enumerate(case):
                if sale >= user[0]:
                    tmp += emoticons[idx] * (100 - sale) // 100
            if tmp >= user[1]:
                result[0] += 1
            else:
                result[1] += tmp
        answer.append(result)
    return max(answer)