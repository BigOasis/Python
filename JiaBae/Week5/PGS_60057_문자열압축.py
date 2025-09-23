def solution(s):
    n = len(s)
    shortest_len = n
    
    # 1 ~ max_n까지 길이로 잘랐을 때
    for cut in range(1, n//2 +1):
        cur = 0
        # 연속된 것 count
        cnt = 1
        st = ""
        while cur + 2 * cut <= n:
            left = s[cur : cur+cut]
            right = s[cur+cut: cur+2*cut]
            
            # 앞의 것과 뒤의 것이 같으면
            if left == right:
                cnt += 1
            # 앞의 것과 뒤의 것이 다르면
            else:
                st += (str(cnt) if cnt > 1 else '') + left
                # 초기화
                cnt = 1
                
            # 시작점 변환
            cur += cut
        
        # 마지막 블록 처리
        st += (str(cnt) if cnt > 1 else '') + s[cur:cur+cut]
            
        st += s[cur+cut:]
        shortest_len = min(shortest_len, len(st))

    return shortest_len