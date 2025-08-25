from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num_list = []
        for i in range(1, n+1): # 조합 만들 배열 우선 만들기
            num_list.append(i)
        
        nCk = combinations(num_list, k) # 조합 만들기
        answer = []
        for element in nCk: # 조합은 각각 튜플, 모두 배열로 바꿔주기
            answer.append(list(element))

        return answer