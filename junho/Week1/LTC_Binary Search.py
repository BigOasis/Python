class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 # 시작점
        end = len(nums) - 1 # 끝점

        while start <= end: # start, end가 만날 때까지 반복 (만나는 경우에도 마지막으로 한 번 확인해야 한다)
            if nums[(start + end) // 2] < target:
                start = (start + end) // 2 + 1
            elif nums[(start + end) // 2] > target:
                end = (start + end) // 2 - 1
            else: # 이 경우는, target을 찾은 경우밖에 X
                return (start + end) // 2

        # while문을 탈출해서 여기까지 온 거라면, target 못 찾은 거임
        return -1