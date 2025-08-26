"""
leetcode: Two Sum
시간복잡도 : O(n)
해시맵 사용
"""
class Solution(object):
    def twoSum(self, nums, target):
        # for문을 한 번만 돌기 위해 이전의 값(num과 인덱스)를 저장할 딕셔너리
        hashmap = {}
        for i, num in enumerate(nums) :
            complement = target - num
            if complement in hashmap :
                return [hashmap[complement], i]
            hashmap[num] = i
                    
        