def solution(relation):
    row_count = len(relation) # 세로 길이
    col_count = len(relation[0]) # 가로 길이
    
    unique_keys = []
    
    def find_subsets(index, current_subset): # col의 인덱스로 subset을 만들어낸다
        # 유일성만 먼저 검사하고, 유일성을 만족하는 모든 키를 일단 모아야 한다
        if current_subset:
            is_unique = check_uniqueness(current_subset, relation, row_count)
            if is_unique:
                unique_keys.append(current_subset)
        
        # 재귀 호출: 다음 속성을 포함하거나 포함하지 않음
        if index < col_count:
            # 1. 현재 속성을 포함하는 경우
            find_subsets(index + 1, current_subset + [index])
            # 2. 현재 속성을 포함하지 않는 경우
            find_subsets(index + 1, current_subset)
            
    # 유일성 검사 함수
    def check_uniqueness(subset, relation, row_count):
        current_tuples = set()
        for row in relation:
            temp_tuple = tuple(row[col] for col in subset)
            current_tuples.add(temp_tuple)
        return len(current_tuples) == row_count

    # 1단계: 모든 유일한 키 찾기
    find_subsets(0, [])

    # 2단계: 최소성 검사
    # 속성 개수(리스트 길이)가 적은 순서대로 정렬
    unique_keys.sort(key=len)
    
    candidate_keys = []
    
    for unique_key in unique_keys:
        is_minimal = True
        for candidate_key in candidate_keys:
            # 현재 유일한 키가 이미 찾은 후보키의 슈퍼셋인지 확인
            if set(candidate_key).issubset(set(unique_key)):
                is_minimal = False
                break
        
        if is_minimal:
            candidate_keys.append(unique_key)
            
    return len(candidate_keys) # 결과 반환