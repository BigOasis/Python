def solution(new_id):
    # 1단계
    s = new_id.lower()
    
    # 2단계
    pass_ch = []
    for ch in s:
        if ch.islower() or ch.isdigit() or ch in ['-', '_', '.']:
            pass_ch.append(ch)
    s = ''.join(pass_ch)
    
    # 3단계
    compact = []
    for ch in s:
        if ch == "." and compact and compact[-1] == "." :
            continue
        compact.append(ch)
    s = ''.join(compact)
    
    # 4단계
    s = s.strip(".")
    
    # 5단계
    if not s : s = 'a'
    
    # 6단계
    if len(s) >= 16 : 
        s = s[:15].rstrip('.')
    
    # 7단계
    while len(s) < 3:
        s += s[-1]
        
    return s
            