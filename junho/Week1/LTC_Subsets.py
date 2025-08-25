from itertools import combinations

# 비트 마스킹으로 더 빠르게 푸는 방법도 있다고 하는데, 그것도 나중에 한 번 시도해 볼게요
# 아래는 combinations을 1부터 len(nums)까지 돌려서 시도하는 방식입니다 (조금 느린 방식임)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 부분집합을 구하는 것은.. 공집합부터 길이가 len(nums)인 조합을 모두 구하는 것이다 (순서 고려 안하니깐)
        answer = []
        nums_len = len(nums)
        subsets = []
        subsets.append([]) # 우선 공집합 하나 넣어 놓는다
        
        for i in range(1, nums_len+1): 
            nCi = combinations(nums, i)
            for element in nCi: # 모두 넣어 놓는다 (하나씩 넣어야 한다)
                subsets.append(element)
        
        for element in subsets: # subsets의 요소는 모두 튜플, 리스트로 바꿔야 한다
            answer.append(list(element))