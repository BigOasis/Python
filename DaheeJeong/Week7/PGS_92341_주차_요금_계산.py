from collections import defaultdict

def solution(fees, records):
    answer = []
    car_dict = {}
    car_time = defaultdict(int)

    for record in records:
        time, car, status = record.split()
        hour, minute = time.split(":")
        time = int(hour) * 60 + int(minute)

        if status == 'IN':
            car_dict[car] = time

        elif status == 'OUT':
            car_time[car] += time - car_dict[car]
            del car_dict[car]

    end_time = 23 * 60 + 59
    for car, t in car_dict.items():
        car_time[car] += end_time - t

    basic = fees[0]
    basic_money = fees[1]
    unit = fees[2]
    unit_money = fees[3]

    for car, t in car_time.items():
        cost = basic_money
        if t <= basic:
            answer.append((car, cost))
        else:
            t -= basic
            if t % unit != 0:
                cost += (t // unit + 1) * unit_money
            else:
                cost += t // unit * unit_money
            answer.append((car, cost))

    answer = sorted(answer, key=lambda x: x[0])
    ans = []
    for i in range(len(answer)):
        ans.append(answer[i][1])

    return ans