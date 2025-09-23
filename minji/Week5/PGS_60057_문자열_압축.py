def solution(s: str) -> int:
    if len(s) == 1:
        return 1
    
    answer = len(s)
    
    for cut in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[:cut]
        count = 1
        
        for i in range(cut, len(s), cut):
            now = s[i:i+cut]
            if prev == now:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = now
                count = 1
        
        compressed += (str(count) + prev) if count > 1 else prev
        answer = min(answer, len(compressed))
    
    return answer
