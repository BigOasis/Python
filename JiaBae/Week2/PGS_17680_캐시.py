from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0 :
        return 5 * len(cities)
    
    for city in cities :
        c = city.lower()
        
        # 캐시 히트
        if c in cache :
            answer += 1
            cache.remove(c)
            cache.append(c)
        # 캐시 미스
        else :
            answer += 5
            if len(cache) == cacheSize :
                cache.popleft()
            cache.append(c)
    return answer