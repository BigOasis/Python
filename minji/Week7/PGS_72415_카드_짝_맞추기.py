# 카드 짝 맞추기
# BFS + 완전탐색 아아아악 permutations으로 백트레킹대체
# ctrl 이동 포함해서 최단거리 구해야 함
from itertools import permutations
import copy
from collections import deque

# 4. BFS 함수 따로 빼서 만들기: 일반 이동 + ctrl 이동 처리
def bfs(board, start, end):
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[False]*4 for _ in range(4)]
    visited[start[0]][start[1]] = True
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    # 이어서 .... ctrl 이동 함수랑 일반이동 처리하기
    

def solution(board, r, c):
    # 1. 카드 번호별 좌표 저장
    cards = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                num = board[i][j]
                if num not in cards:
                    cards[num] = []
                cards[num].append((i, j))
    
     
    # 2. 카드 순서 전부 탐색해보기
    orders = list(permutations(cards.keys(), len(cards)))
    min_cnt = float('inf')
    
    for order in orders:
        temp = copy.deepcopy(board)
        now_r, now_c = r, c
        total = 0

        for num in order:
            first, second = cards[num]

            # BFS로 두 카드 순서 거리 계산
            dist1 = bfs(temp, (now_r, now_c), first) + bfs(temp, first, second) + 2
            dist2 = bfs(temp, (now_r, now_c), second) + bfs(temp, second, first) + 2

            # 더 짧은 쪽 선택
            if dist1 <= dist2:
                total += dist1
                now_r, now_c = second
            else:
                total += dist2
                now_r, now_c = first

            # 카드 제거 (보드 갱신)
            temp[first[0]][first[1]] = 0
            temp[second[0]][second[1]] = 0

        min_cnt = min(min_cnt, total)
    
    return min_cnt