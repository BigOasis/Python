"""
프로그래머스 캐시
18분

LRU: 가장 최근에 사용되지 않은 것을 빼야함
"""


def solution(cacheSize, cities):
    caches = []
    time = 0

    if cacheSize == 0:
        return len(cities) * 5

    for c in cities:
        lc = c.lower()
        # 캐시히트: 이미 존재한다면
        if lc in caches:
            time += 1
            caches.remove(lc)
            caches.append(lc)
        # 캐시미스: 없으면 추가 및 LRU
        else:
            time += 5
            caches.append(lc)

            if len(caches) > cacheSize: caches.pop(0)

    return time
