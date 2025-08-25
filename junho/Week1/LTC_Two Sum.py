# 보통 해시맵을 이용해서 푼다고 한다.
# 해시맵을 이용해서 풀면, O(n)으로 (한 번의 순회)만을 통해서 문제를 풀 수 있거든!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_idx = {}
        for i, num in enumerate(nums): # nums 배열 순회
            complement = target - num
            if complement in num_and_idx: # 보완값이 이미 num_and_idx에 있어요?
                return [num_and_idx[complement], i]
            # 없으면, num_and_idx에 넣어주자
            num_and_idx[num] = i