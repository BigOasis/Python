from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  # 빈 배열이면 바로 0
            return 0
        
        num_set = set(nums) # 중복 제거 및 O(1) 탐색을 위해 집합으로 변환
        best = 0 
        
        for n in num_set:
            # 앞 숫자가 없으면 연속 시작점
            if n - 1 not in num_set:
                length = 1
                now = n
                # 연속된 숫자가 이어지는 동안 카운트 증가
                while now + 1 in num_set:
                    now += 1
                    length += 1

                best = max(best, length)
        
        return best
