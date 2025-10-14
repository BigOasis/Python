# 주어진 순열의 k번째 순열을 찾는 문제
# 1부터 n까지의 숫자를 이용해 만들 수 있는 순열은 총 n!개
# 순열을 다 찾지 말고 k가 속한 구간을 찾아가면서 k번째 순열을 찾기

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1부터 n까지의 숫자 리스트 생성
        nums = [str(i) for i in range(1, n + 1)]
        
        # 팩토리얼 계산을 위한 함수
        from math import factorial
        
        # k를 0-based 인덱스로 변환
        k -= 1
        
        result = ""
        
        # 자리수별로 숫자 선택
        for i in range(n, 0, -1):
            group = factorial(i - 1)    # 각 숫자가 만드는 순열의 개수
            index = k // group          # 이번 자리에 올 숫자의 인덱스
            result += nums.pop(index)   # 해당 숫자를 결과에 추가
            k %= group                  # 남은 순열 내 위치 갱신
        
        return result
