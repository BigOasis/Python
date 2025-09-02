from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()

        if city in cache:
            cache.remove(city)  # 기존 위치 제거
            cache.append(city)  # 가장 최근에 사용된 것으로 갱신
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()     # 가장 오랜된거 제거
            cache.append(city)      # 현재 시티로 갱신
            answer += 5

    return answer

#     선입 선출 cacheSize만큼 우선 시티를 넣고 무조건 +5
#     만약 다음 께 없으면 leffpop 하고 그 시티를 다시 집어 넣고
#     queue에 넣어 질떄마다 +5 만약에 있으면 +1
#     해당 코드는 오류 처음부터 끝까지 하나씩 처리하는 코드로 수정
    
    
    
#     # 1. 초기 캐시 채우기
#     for i in range(min(cacheSize, len(cities))):
#         city = cities[i].lower()
#         cache.append(city)
#         answer += 5  # 무조건 miss
        
        
#     # 2. 나머지 도시 순회
#     for i in range(cacheSize, len(cities)):
#         city = cities[i].lower()

#         if city in cache:
#             cache.remove(city)  # 기존 위치 제거
#             cache.append(city)  # 가장 최근에 사용된 것으로 갱신
#             answer += 1
#         else:
#             # cache miss
#             cache.popleft()     # 가장 오랜된거 제거
#             cache.append(city)  # 현재 시티로 갱신
#             answer += 5

#     return answer