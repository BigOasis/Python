from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        k -= 1 # 밑의 while문을 보기 편하게 하기 위해서, 1 빼고 시작해준다
        ret = ''
        while k > 0: # k가 0보다 큰 동안은 계속!
            x = factorial(n-1)
            if k >= x: # k가 x보다 무조건 크거나 같아야 함 (아니면, 밑의 과정을 하는 의미 X)
                quotient = k // x
                k -= quotient * x 
                ret += nums.pop(quotient) # nums 배열에서, 해당 자리에 있는거 뽑아내기
            else: # k가 x보다 작은 경우 -> quotient가 0이 나오는 경우 -> 현재 자리 숫자 고정
                ret += nums.pop(0) # 현재 자리 숫자 중 맨 앞자리 빼내서 ret에 삽입
            n -= 1 # 비교할 자릿수 -1
        ret += ''.join(nums) # while문 빠져나옴, k값 모두 소진, nums 남은 거 그냥 다 붙여버리면 그만
        return ret