"""
leetcode: Palindrome_Partitioning
시간복잡도 : 
시간 초과나서 아직 못 품 -> dp로 변경해야함 
"""
class Solution(object):
    def partition(self, s):
        result = []
        path = []

        def is_pal(i, j) :
            while i < j :
                if s[i] != s[j] :
                    return False
                    i += 1
                    j -= 1

            return True
        
        def dfs(i) :
            # 끝나는 조건
            if i == len(s) :
                result.append(path[:])
                return 

            for j in range(i, len(s)) :
                if is_pal(i, j) :
                    path.append(s[i:j+1]) 
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return result