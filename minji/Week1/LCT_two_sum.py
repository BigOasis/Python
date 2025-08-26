class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(f"i={i}, j={j}, nums[{i}]={nums[i]}, nums[{j}]={nums[j]}, 합={nums[i] + nums[j]}")
                if nums[i] + nums[j] == target:
                    print("타겟과 같은 값을 찾음!", i, j)  
                    return [i, j]

s = Solution()
result = s.twoSum([2, 7, 11, 15], 9)
print("결과:", result)
