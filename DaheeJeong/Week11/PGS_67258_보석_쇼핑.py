from collections import defaultdict


def solution(gems):
    total = len(set(gems))
    gem_dict = defaultdict(int)
    answer = [0, len(gems) - 1]
    start = 0

    for end, gem in enumerate(gems):
        gem_dict[gem] += 1

        # 모든 종류 포함 시 구간 줄이기
        while len(gem_dict) == total:
            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]

            # 왼쪽 보석 제거 시도
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1

    return [answer[0] + 1, answer[1] + 1]