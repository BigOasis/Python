from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}  # 숫자랑 위치 저장할 딕셔너리
        
        for i in range(len(nums)):
            now = nums[i]                  # 지금 보고 있는 숫자
            find = target - now            # 필요한 숫자
            
            if find in check:              # 필요한 숫자가 이미 있으면
                return [check[find], i]    # 그 위치랑 지금 위치 반환
            
            check[now] = i                 # 못 찾았으면 기록해둠
