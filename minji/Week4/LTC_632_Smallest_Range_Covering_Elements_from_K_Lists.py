import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float('-inf')

        # 초기 힙 구성 및 최대값 설정
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], i, 0))
            current_max = max(current_max, lst[0])

        best_range = [float('-inf'), float('inf')]

        while True:
            val, list_idx, elem_idx = heapq.heappop(heap)

            if current_max - val < best_range[1] - best_range[0]:
                best_range = [val, current_max]

            # 다음 원소가 없으면 종료
            if elem_idx + 1 == len(nums[list_idx]):
                break

            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)

        return best_range
