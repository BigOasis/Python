def solution(today, terms, privacies):
    answer = []
    
    # 날짜를 일수로 변환하는 함수
    def convert_to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return d + 28 * m + 28 * 12 * y
    
    # 약관 유효기간 매핑 
    term_month = {}
    for t in terms:
        term, month = t.split()
        term_month[term] = int(month)
        
    for idx, p in enumerate(privacies):
        date_str, term = p.split()
        start_days = convert_to_days(date_str)
        expire_days = start_days + term_month[term] * 28
        today_days = convert_to_days(today)
        
        if expire_days <= today_days:
            answer.append(idx+1)
    
    return answer
        