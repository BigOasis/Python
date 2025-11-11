def solution(today, terms, privacies):
    today = "".join(today.split("."))

    dic_terms = {}
    for term in terms:
        term_type, term_month = term.split()
        dic_terms[term_type] = int(term_month)

    answer = []

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split("."))

        month += dic_terms[term]

        if month % 12 == 0:
            year = year + (month // 12) - 1
            month = 12
        else:
            year = year + month // 12
            month = month % 12

        year, month, day = str(year), str(month), str(day)
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        expired_date = year + month + day
        if today >= expired_date:
            answer.append(i + 1)

    return answer