"""
백준 11725번: 트리의 부모 찾기
"""

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n+1)
q = deque([1])
parent[1] = -1

# BFS
while q:
    a = q.popleft()
    for v in tree[a]:
        if parent[v] == 0:
            parent[v] = a
            q.append(v)

for i in range(2, n+1):
    print(parent[i])
