# 그냥 단순하게 영어를 숫자로 치환

def solution(s):
    num_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    for word, digit in num_map.items():
        s = s.replace(word, digit)
    
    return int(s)
