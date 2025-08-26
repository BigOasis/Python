from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permu_list = []
        nums_len = len(nums)
        nPr = permutations(nums, nums_len)
        for element in nPr: # 순열 하나씩 순회하며 그거 list로 바꾸고 permu_list에 집어 넣기(최초는 튜플로 되어 있거든...)
            permu_list.append(list(element))
        
        return permu_list