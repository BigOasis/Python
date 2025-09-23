def solution(today, terms, privacies):
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y*12*28 + m*28 + d
    
    today_num = to_days(today)
    print("오늘:", today_num)
    
    term_dict = {}
    for t in terms:
        name, months = t.split()
        term_dict[name] = int(months)
    print("약관:", term_dict)  # 확인
    
    answer = []
    
    for i, p in enumerate(privacies, start=1):
        date, kind = p.split()
        start_num = to_days(date)
        expire = start_num + term_dict[kind]*28
        
        print(i, date, kind, "->", start_num, "만료:", expire)
        
        # 오늘이 만료일 이상이면 파기 대상
        if expire <= today_num:
            answer.append(i)

    print("최종:", answer)

    return answer
