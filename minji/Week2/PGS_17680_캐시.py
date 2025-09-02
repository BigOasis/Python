# 캐시 크기와 도시이름이 주어지고 선입선출방식으로 동작
# hit는 time 1, miss는 time 5
# 도시이름은 대소문자 구분없이 처리
# 최종 time 구하기

def solution(cacheSize, cities):
    time = 0
    cache = []

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower() # 대소문자 처리안한댔으니까 다 소문자처리
        if city in cache:  # cache hit
            time += 1
            cache.remove(city)  # 위치 갱신을 위해 지움
            cache.append(city)
        else:  # cache miss
            time += 5
            if len(cache) >= cacheSize:
                cache.pop(0)  # 가장 오래된 놈 제거 (선입선출!!!)
            cache.append(city)

    return time