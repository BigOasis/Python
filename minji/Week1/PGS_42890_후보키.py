from itertools import combinations

def solution(relation):
    num_rows = len(relation)
    num_cols = len(relation[0])
    result = []

    for size in range(1, num_cols + 1):
        for cols in combinations(range(num_cols), size):
            unique_values = {tuple(row[col] for col in cols) for row in relation}
            if len(unique_values) != num_rows:
                continue

            if any(set(key).issubset(cols) for key in result):
                continue
            result.append(cols)

    return len(result)
