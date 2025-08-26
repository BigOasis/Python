class Solution:
    def partition(self, s):
        result = []     # 최종 결과를 담을 리스트
        path = []       # 현재까지의 분할 경로

        # 팰린드롬 판별 함수
        def is_palindrome(word):
            return word == word[::-1]

        # DFS + 백트래킹
        def backtrack(start_index):
            if start_index == len(s):       # 문자열 끝까지 도달
                result.append(path[:])      # 현재 경로를 복사해서 저장
                return
            for end_index in range(start_index, len(s)):
                piece = s[start_index:end_index+1]  # 부분 문자열
                if is_palindrome(piece):            # 팰린드롬이면
                    path.append(piece)              # 선택
                    backtrack(end_index + 1)        # 다음 탐색
                    path.pop()                      # 선택 취소 (백트래킹)

        backtrack(0)
        return result
