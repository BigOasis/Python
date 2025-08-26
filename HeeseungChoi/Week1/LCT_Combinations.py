from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        choose = []

        def backtrack(start: int, level: int):
            if level == k:
                result.append(choose[:])
                return

            for i in range(start, n + 1):
                choose.append(i)
                backtrack(i + 1, level + 1)
                choose.pop()

        backtrack(1, 0)
        return result