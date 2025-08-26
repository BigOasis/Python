from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []         # 결과 저장
        choose = []         # 현재 선택된 숫자들
        check = [False] * len(nums)  # 숫자 사용 여부 추적

        def backtrack(level):
            if level == len(nums):   # 모든 숫자 선택 완료
                result.append(choose[:])  # 복사해서 저장
                return

            for i in range(len(nums)):
                if check[i]:
                    continue

                choose.append(nums[i])
                check[i] = True
                backtrack(level + 1)
                check[i] = False
                choose.pop()

        backtrack(0)
        return result          



        