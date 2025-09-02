from collections import deque


def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5

    caches = deque(maxlen=cacheSize)
    cities = map(lambda x: x.lower(), cities)

    for city in cities:
        if city not in caches:
            answer += 5
        else:
            answer += 1
            caches.remove(city)

        caches.append(city)

    return answer