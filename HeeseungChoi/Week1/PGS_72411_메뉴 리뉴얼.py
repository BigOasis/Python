# 배열에 한개의 문자열을 조합으로 만듦
def make_combinations(chars, comb, start, depth, result):
    if len(comb) == depth:
        result.append(''.join(comb))
        return
    
    for i in range(start, len(chars)):
        comb.append(chars[i])
        make_combinations(chars, comb, i + 1, depth, result)
        comb.pop()

def solution(orders, course):
    answer = []
    
# 코스 길이에 따른 조합 반복
    for c in course:
        comb_counter = {}

 # 각 주문에 대해 조합 생성
        for order in orders:
            chars = sorted(list(order))
            temp_combs = []
            # 정렬된 주문에서 c개짜리 조합 생성
            make_combinations(chars, [], 0, c, temp_combs)

            # 조합 등장 횟수 기록
            for comb in temp_combs:
                if comb in comb_counter:
                    comb_counter[comb] += 1
                else:
                    comb_counter[comb] = 1

         # 2명 이상이 주문한 조합 중에서 가장 많이 등장한 횟수 찾기
        max_count = 0
        for count in comb_counter.values():
            if count >= 2:
                max_count = max(max_count, count)
                
         # 가장 인기 있는 조합(등장 횟수 == max_count)만 answer에 추가
        for comb, count in comb_counter.items():
            if count == max_count and count >= 2:
                answer.append(comb)

    return sorted(answer)